#!/usr/bin/env python3
"""Extract non-built-in plugin metadata; never reads personal YAML or credentials."""
import argparse
import json
from pathlib import Path


def resolve(parent, name):
    for root in [parent, *parent.parents]:
        path = root / 'node_modules' / name
        if (path / 'package.json').is_file():
            return path.resolve()
    return None


def inventory(profile):
    manifest = json.loads((profile / 'package.json').read_text(encoding='utf-8'))
    bundles = manifest.get('dsh', {}).get('profile', {}).get('bundles', [])
    queue = [(name, profile) for name in dict.fromkeys(bundles + list(manifest.get('dependencies', {})))]
    seen, packages = set(), []
    for name, parent in queue:
        if name in seen or name.startswith('@deepseek-ai/'):
            continue
        seen.add(name)
        path = resolve(parent, name)
        if path is None:
            if name in bundles:
                packages.append({'name': name, 'status': 'unresolved', 'topLevel': True})
            continue
        data = json.loads((path / 'package.json').read_text(encoding='utf-8'))
        dsh = data.get('dsh', {})
        if not dsh.get('bundle') and not dsh.get('client'):
            continue
        # Allowlist fields; avoid local link targets, environment and config.
        packages.append({key: data[key] for key in ['name', 'version', 'description', 'author', 'contributors', 'repository', 'license'] if key in data} | {'topLevel': name in bundles, 'status': 'installed-not-runtime-tested'})
        for child in data.get('dependencies', {}):
            if not child.startswith('@deepseek-ai/'):
                queue.append((child, path))
    return {'schemaVersion': 1, 'scope': 'non-built-in DSH plugin packages', 'packages': packages}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--output', required=True, help='New JSON output file; existing files are refused.')
    args = parser.parse_args()
    result = inventory(Path(args.profile).expanduser().resolve())
    with Path(args.output).expanduser().open('x', encoding='utf-8') as output:
        json.dump(result, output, ensure_ascii=False, indent=2)
        output.write('\n')
    print(f'Inventoried {len(result["packages"])} non-built-in plugins.')

if __name__ == '__main__':
    main()
