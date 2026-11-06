#!/usr/bin/env python3
"""Validate the target OS, Python architecture and optional Node architecture."""
import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess


def normalize_arch(machine):
    value = machine.lower()
    return {'x86_64': 'x64', 'amd64': 'x64', 'aarch64': 'arm64'}.get(value, value)


def validate_runtime(spec, system=None, machine=None, node_info=None):
    system = system or platform.system()
    architecture = normalize_arch(machine or platform.machine())
    if system != spec['system'] or architecture != spec['architecture']:
        raise ValueError(f"This repository requires {spec['system']} {spec['architecture']}; current runtime is {system} {architecture}. Use the matching platform repository.")
    if node_info is not None:
        node_system, node_arch = node_info.strip().split(':', 1)
        expected_node = 'win32' if spec['system'] == 'Windows' else 'darwin'
        if node_system != expected_node or node_arch != spec['architecture']:
            raise ValueError(f"Node requires {expected_node}:{spec['architecture']}; detected {node_info.strip()}. Install the native Node build for this repository.")
    return {'system': system, 'architecture': architecture, 'target': spec['id'], 'node': node_info}


def get_node_info():
    node = shutil.which('node')
    if not node:
        raise ValueError('Node is not on PATH. Install the native Node build first.')
    return subprocess.check_output([node, '-p', 'process.platform + ":" + process.arch'], text=True).strip()


def manager_command(manager, arguments, system=None):
    # Arguments are fixed install switches, not user-authored shell fragments.
    if (system or platform.system()) == 'Windows' and Path(manager).suffix.lower() in {'.cmd', '.bat'}:
        # Official npm/global pnpm layouts expose a JS entry beside the shim.
        # Running Node directly avoids cmd.exe quoting and execution-policy issues.
        entries = {'npm': ('npm', 'npm-cli.js'), 'pnpm': ('pnpm', 'pnpm.cjs')}
        identity = Path(manager).stem.lower()
        if identity in entries:
            package, script = entries[identity]
            entry = Path(manager).parent / 'node_modules' / package / 'bin' / script
            node = shutil.which('node')
            if entry.is_file() and node:
                return [node, str(entry), *arguments]
        command = '""' + str(manager) + '" ' + ' '.join(arguments) + '"'
        return [os.environ.get('COMSPEC', 'cmd.exe'), '/d', '/s', '/c', command]
    return [str(manager), *arguments]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-node', action='store_true')
    args = parser.parse_args()
    spec = json.loads((Path(__file__).resolve().parents[1] / 'platform.json').read_text(encoding='utf-8'))
    try:
        report = validate_runtime(spec, node_info=get_node_info() if args.check_node else None)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Platform check failed: {exc}\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
