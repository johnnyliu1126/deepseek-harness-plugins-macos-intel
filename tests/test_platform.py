import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PlatformTest(unittest.TestCase):
    def load_support(self):
        source = ROOT / 'scripts' / 'platform_support.py'
        self.assertTrue(source.exists(), 'Platform validation helper must exist')
        spec = importlib.util.spec_from_file_location('platform_support_under_test', source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_accepts_matching_native_runtime(self):
        module = self.load_support()
        expected = json.loads((ROOT / 'platform.json').read_text())
        machine = 'AMD64' if expected['architecture'] == 'x64' else 'aarch64'
        os_id = 'win32' if expected['system'] == 'Windows' else 'darwin'
        report = module.validate_runtime(expected, expected['system'], machine, os_id + ':' + expected['architecture'])
        self.assertEqual(report['architecture'], expected['architecture'])

    def test_rejects_wrong_os(self):
        module = self.load_support()
        expected = json.loads((ROOT / 'platform.json').read_text())
        with self.assertRaisesRegex(ValueError, 'requires'):
            module.validate_runtime(expected, 'Linux', 'x86_64')

    def test_rejects_wrong_cpu(self):
        module = self.load_support()
        expected = json.loads((ROOT / 'platform.json').read_text())
        wrong = 'arm64' if expected['architecture'] == 'x64' else 'x86_64'
        with self.assertRaisesRegex(ValueError, 'requires'):
            module.validate_runtime(expected, expected['system'], wrong)

    def test_rejects_node_architecture_mismatch(self):
        module = self.load_support()
        expected = json.loads((ROOT / 'platform.json').read_text())
        wrong = 'arm64' if expected['architecture'] == 'x64' else 'x64'
        os_id = 'win32' if expected['system'] == 'Windows' else 'darwin'
        with self.assertRaisesRegex(ValueError, 'Node'):
            module.validate_runtime(expected, expected['system'], expected['architecture'], os_id + ':' + wrong)

    def test_windows_cmd_path_is_quoted(self):
        module = self.load_support()
        command = module.manager_command(r'C:\Program Files\nodejs\npm.cmd', ['install', '--ignore-scripts'], system='Windows')
        self.assertIn('/c', command)
        self.assertIn('"C:\\Program Files\\nodejs\\npm.cmd"', command[-1])

    def test_windows_npm_uses_native_node_entry_when_available(self):
        module = self.load_support()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manager = root / 'npm.cmd'
            entry = root / 'node_modules' / 'npm' / 'bin' / 'npm-cli.js'
            entry.parent.mkdir(parents=True)
            entry.write_text('// fixture')
            command = module.manager_command(str(manager), ['install', '--ignore-scripts'], system='Windows')
            self.assertEqual(command[1], str(entry))
            self.assertNotIn('/c', command)

    def test_catalog_has_no_excluded_packages(self):
        expected = json.loads((ROOT / 'platform.json').read_text())
        names = {p['name'] for p in json.loads((ROOT / 'catalog.lock.json').read_text())['packages']}
        self.assertTrue(names.isdisjoint(expected['excludedPackages']))
        self.assertFalse(any(n.startswith('@deepseek-ai/') for n in names))

if __name__ == '__main__':
    unittest.main()
