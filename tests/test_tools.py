import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ToolTest(unittest.TestCase):
    def test_inventory_excludes_builtins_and_ignores_private_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile = Path(tmp) / 'profile'
            profile.mkdir()
            deps = {'dsh-demo': '1.2.3', '@deepseek-ai/dsh-base': '0.2.1-rc.4'}
            (profile / 'package.json').write_text(json.dumps({'dependencies': deps, 'dsh': {'profile': {'bundles': list(deps)}}}))
            (profile / 'cordis.patch.yml').write_text('DO NOT READ PRIVATE CONFIGURATION\n')
            for name in deps:
                pkg = profile / 'node_modules' / name
                pkg.mkdir(parents=True)
                (pkg / 'package.json').write_text(json.dumps({'name': name, 'version': deps[name], 'dsh': {'bundle': {'patch': './cordis.patch.yml'}}}))
            output = Path(tmp) / 'inventory.json'
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/inventory.py'), '--profile', str(profile), '--output', str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = json.loads(output.read_text())['packages']
            self.assertEqual([p['name'] for p in rows], ['dsh-demo'])
            self.assertNotIn('PRIVATE CONFIGURATION', output.read_text())

    def test_scanner_rejects_secret_without_echoing_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            secret = 'gh' + 'p_' + 'x' * 36
            (Path(tmp) / 'example.txt').write_text(secret)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check.py'), '--root', tmp, '--scan-only'], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('credential', result.stderr.lower())
            self.assertNotIn(secret, result.stderr + result.stdout)

    def test_scanner_accepts_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'example.md').write_text('Set VISION_API_KEY locally; never commit credentials.\n')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check.py'), '--root', tmp, '--scan-only'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

if __name__ == '__main__':
    unittest.main()
