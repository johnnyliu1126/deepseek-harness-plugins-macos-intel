#!/usr/bin/env python3
"""Create a fresh DSH plugin profile; default is a read-only plan.

Never merges into an existing profile. Third-party roots are downloaded from
pinned upstream URLs and verified against the catalog's SRI before installation.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from platform_support import validate_runtime, get_node_info, manager_command


def selected_packages(catalog, names, all_plugins):
    packages = {p['name']: p for p in catalog['packages']}
    selected = [p for p in packages.values() if p['topLevel']] if all_plugins else []
    for name in names:
        if name not in packages:
            raise ValueError(f'Unknown plugin: {name}')
        if packages[name] not in selected:
            selected.append(packages[name])
    if not selected:
        raise ValueError('Select --all or --plugins NAME [NAME ...].')
    chosen = {p['name'] for p in selected}
    family = {n for n in packages if n.startswith('@neystan/')}
    if '@neystan/dsh-web-ui-all' in chosen and chosen & (family - {'@neystan/dsh-web-ui-all'}):
        raise ValueError('Aggregate and child plugins cannot be installed together.')
    if '@neystan/dsh-skins' in chosen and '@neystan/dsh-client-ui-skin-center' in chosen:
        raise ValueError('Aggregate dsh-skins and child skin-center cannot be installed together.')
    return selected


def download_verified(url, integrity, destination):
    if not url.startswith('https://'):
        raise ValueError('Only HTTPS distribution URLs are accepted.')
    algorithm, encoded = integrity.split('-', 1)
    if algorithm not in ('sha512', 'sha256'):
        raise ValueError(f'Unsupported integrity algorithm: {algorithm}')
    hasher = hashlib.new(algorithm)
    request = urllib.request.Request(url, headers={'Accept-Encoding': 'identity', 'Cache-Control': 'no-cache'})
    downloaded = 0
    with urllib.request.urlopen(request, timeout=60) as response, destination.open('xb') as output:
        expected_length = response.headers.get('Content-Length')
        while True:
            block = response.read(1024 * 1024)
            if not block:
                break
            output.write(block)
            hasher.update(block)
            downloaded += len(block)
    if expected_length is not None and downloaded != int(expected_length):
        raise ValueError(f'Incomplete download for {destination.name}; retry with a new target.')
    if hasher.digest() != base64.b64decode(encoded, validate=True):
        raise ValueError(f'Integrity mismatch for {destination.name}')


def build(args):
    catalog = json.loads((ROOT / 'catalog.lock.json').read_text(encoding='utf-8'))
    selected = selected_packages(catalog, args.plugins, args.all)
    target = Path(args.target).expanduser().absolute()
    if target.exists() or target.is_symlink():
        raise ValueError(f'Target already exists; choose a new profile: {target}')
    if args.fetch and not args.apply:
        raise ValueError('--fetch requires --apply.')
    plan = {'target': str(target), 'write': args.apply, 'fetch': args.fetch,
            'packages': [p['name'] + '@' + p['version'] for p in selected],
            'hostBundles': catalog['hostBundles'],
            'note': 'Built-in host code is not copied. Existing profiles are never overwritten.'}
    spec = json.loads((ROOT / 'platform.json').read_text(encoding='utf-8'))
    plan['targetPlatform'] = spec['id']
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    if not args.apply:
        return
    validate_runtime(spec, node_info=get_node_info() if args.fetch else None)
    manager = shutil.which(args.manager) if args.fetch else None
    if args.fetch and not manager:
        raise ValueError(f'Package manager is not on PATH: {args.manager}')
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.collection-stage-', dir=target.parent))
    try:
        deps = {}
        vendor = stage / 'vendor'
        for p in selected:
            if p['kind'] == 'local':
                local = ROOT / 'plugins' / p['name']
                if not (local / 'package.json').is_file():
                    raise ValueError(f'Missing local source: {p["name"]}')
                deps[p['name']] = 'file:' + str(local)
            elif args.fetch:
                dist = p['distribution']
                vendor.mkdir(exist_ok=True)
                archive = vendor / f'{p["slug"]}-{p["version"]}.tgz'
                download_verified(dist['tarball'], dist['integrity'], archive)
                deps[p['name']] = 'file:vendor/' + archive.name
            else:
                deps[p['name']] = p['distribution']['tarball'] if p['name'] == 'dsh-purge-community' else p['version']
        package = {'name': 'dsh-plugin-collection-profile', 'private': True,
                   'dependencies': deps,
                   'dsh': {'profile': {'bundles': catalog['hostBundles'] + [p['name'] for p in selected]}}}
        (stage / 'package.json').write_text(json.dumps(package, indent=2) + '\n')
        (stage / 'cordis.yml').write_text('[]\n')
        chosen = {p['name'] for p in selected}
        guards = {
            'ui-task-board': {'@neystan/dsh-web-ui-all', '@neystan/dsh-client-ui-task-board'},
            'pet': {'@neystan/dsh-web-ui-all', '@neystan/dsh-pet'},
            'describe-image': {'@neystan/dsh-web-ui-all', '@neystan/dsh-tool-describe-image'},
            'ui-skin-center': {'@neystan/dsh-web-ui-all', '@neystan/dsh-skins', '@neystan/dsh-client-ui-skin-center'},
        }
        template = (ROOT / 'templates' / 'compatibility.patch.yml').read_text(encoding='utf-8')
        patch = ''.join('- id: ' + block for block in template.split('- id: ')[1:]
                        if chosen & guards[block.splitlines()[0].strip()])
        (stage / 'cordis.patch.yml').write_text(patch or '[]\n', encoding='utf-8')
        receipt = {'snapshotDate': catalog['snapshotDate'], 'plugins': plan['packages'],
                   'catalogSha256': hashlib.sha256((ROOT / 'catalog.lock.json').read_bytes()).hexdigest(),
                   'fetchCompleted': False, 'credentialsIncluded': False,
                   'localSourceRoot': str(ROOT / 'plugins'), 'platform': spec['id']}
        if args.fetch:
            options = ['install', '--ignore-scripts']
            if args.manager == 'npm':
                options.append('--no-audit')
            subprocess.run(manager_command(manager, options), cwd=stage, check=True)
            receipt['fetchCompleted'] = True
        (stage / 'collection-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        # mkdir reserves the name atomically; another process's target is never
        # overwritten, even if it appeared after the initial existence check.
        target.mkdir(exist_ok=False)
        try:
            for child in stage.iterdir():
                child.rename(target / child.name)
        except Exception:
            raise RuntimeError(f'Profile transfer incomplete; inspect {target} and {stage}')
        stage.rmdir()
        print(f'Created: {target}')
        print('Restart/launch DSH with this profile explicitly. No live process was restarted.')
    except Exception:
        print(f'Staging data retained for inspection: {stage}', file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, help='A new profile directory; existing paths are refused.')
    parser.add_argument('--plugins', nargs='+', default=[])
    parser.add_argument('--all', action='store_true', help='All top-level additions; aggregate children are not duplicated.')
    parser.add_argument('--apply', action='store_true', help='Create the new profile; never alters another profile.')
    parser.add_argument('--fetch', action='store_true', help='Verify/download third-party roots and install dependencies.')
    parser.add_argument('--manager', choices=['pnpm', 'npm'], default='pnpm')
    args = parser.parse_args()
    try:
        build(args)
    except (ValueError, OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
