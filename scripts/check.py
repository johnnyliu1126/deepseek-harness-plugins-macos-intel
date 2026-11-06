#!/usr/bin/env python3
"""Check collection docs, provenance, links and likely secrets without echoing values."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.parse

PATTERNS = [
    ('credential token', re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9_-]{20,})')),
    ('private key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
    ('JWT credential', re.compile(r'eyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}')),
    ('personal absolute path', re.compile(r'/' + r'Users/(?!USER(?:/|\b))[^/\s"\']+/')),
]
PRIVATE_NAMES = {'.credentials.yaml', 'hooks.json', 'github-token', 'devices.json', 'server-key.pem', 'ca-key.pem'}
EXCLUDED_PARTS = {'.git', 'node_modules', '__pycache__'}


def files(root):
    return [p for p in root.rglob('*') if p.is_file() and not any(x in EXCLUDED_PARTS for x in p.relative_to(root).parts)]


def scan(root, candidates):
    errors = []
    for path in candidates:
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f'Symlink not allowed in release: {relative}')
            continue
        if path.name in PRIVATE_NAMES or path.suffix in {'.pem', '.key', '.log'} or path.name.startswith('.env'):
            errors.append(f'Private-state filename: {relative}')
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'Unexpected binary in source collection: {relative}')
            continue
        for label, pattern in PATTERNS:
            if pattern.search(text):
                errors.append(f'Potential {label}: {relative}')
    return errors


def validate(root, candidates):
    errors = []
    catalog = json.loads((root / 'catalog.lock.json').read_text(encoding='utf-8'))
    names = set()
    for item in catalog['packages']:
        name = item['name']
        if name in names or name.startswith('@deepseek-ai/'):
            errors.append(f'Duplicate or built-in catalog package: {name}')
        names.add(name)
        directory = root / 'catalog' / item['slug']
        for doc in ['README.md', 'README.zh-CN.md', 'evidence.json']:
            if not (directory / doc).is_file():
                errors.append(f'Missing plugin documentation: {name}/{doc}')
        if not item['features'] or any(not f.get('zh') or not f.get('en') for f in item['features']):
            errors.append(f'Missing paired features: {name}')
        if not item.get('author'):
            errors.append(f'Missing author/provenance statement: {name}')
        if item['kind'] == 'third-party':
            dist = item.get('distribution', {})
            if not dist.get('integrity') or not dist.get('tarball', '').startswith('https://'):
                errors.append(f'Unpinned upstream root: {name}')
            if (root / 'plugins' / name).exists():
                errors.append(f'Unexpected vendored third-party source: {name}')
        else:
            directory = root / 'plugins' / name
            for file, digest in item['files'].items():
                if file == 'package.json':
                    continue  # Explicit private/files packaging edits are documented.
                if hashlib.sha256((directory / file).read_bytes()).hexdigest() != digest:
                    errors.append(f'Imported runtime source changed: {name}/{file}')
    # Check local Markdown links. External references are checked separately;
    # this command never contacts networks or renders remote media.
    for path in candidates:
        if path.suffix != '.md':
            continue
        for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', path.read_text(encoding='utf-8')):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            dest = urllib.parse.unquote(link.split('#', 1)[0])
            if dest and not (path.parent / dest).exists():
                errors.append(f'Broken local link in {path.relative_to(root)}: {dest}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument('--scan-only', action='store_true')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    candidates = files(root)
    errors = scan(root, candidates)
    if not args.scan_only:
        errors += validate(root, candidates)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f'PASS: {len(candidates)} files checked; no detected secrets or validation errors.')
    print('Heuristic scanning is not a guarantee; review the exact staged file list before publishing.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
