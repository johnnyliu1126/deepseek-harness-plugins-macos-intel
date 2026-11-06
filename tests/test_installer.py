import json
import platform
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'collection.py'
SPEC = json.loads((ROOT / 'platform.json').read_text(encoding='utf-8'))
NATIVE = platform.system() == SPEC['system'] and {'x86_64':'x64','AMD64':'x64','aarch64':'arm64'}.get(platform.machine(),platform.machine()) == SPEC['architecture']

class InstallerTest(unittest.TestCase):
    def invoke(self, target, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--target', str(target), *args], capture_output=True, text=True)

    def test_plan_never_writes_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp) / 'profile'
            result = self.invoke(target, '--plugins', 'dsh-restart')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            self.assertIn('dsh-restart', result.stdout)

    @unittest.skipUnless(NATIVE, "requires matching native platform; guard tests run on every host")
    def test_apply_creates_selected_profile_without_touching_other_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = pathlib.Path(tmp) / 'desktop'
            old.mkdir()
            (old / 'cordis.patch.yml').write_text('private: untouched\n')
            target = pathlib.Path(tmp) / 'collection'
            result = self.invoke(target, '--plugins', 'dsh-balance-monitor', '--apply')
            self.assertEqual(result.returncode, 0, result.stderr)
            package = json.loads((target / 'package.json').read_text())
            self.assertEqual(set(package['dependencies']), {'dsh-balance-monitor'})
            self.assertEqual(package['dsh']['profile']['bundles'][-1], 'dsh-balance-monitor')
            self.assertEqual((old / 'cordis.patch.yml').read_text(), 'private: untouched\n')
            self.assertTrue((target / 'collection-receipt.json').exists())
            self.assertEqual((target / 'cordis.patch.yml').read_text(), '[]\n')

    def test_refuses_existing_target_and_preserves_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp)
            sentinel = target / 'package.json'
            sentinel.write_bytes(b'original bytes')
            result = self.invoke(target, '--all', '--apply')
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_bytes(), b'original bytes')

    def test_unknown_plugin_is_rejected_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp) / 'profile'
            result = self.invoke(target, '--plugins', 'nonexistent-plugin', '--apply')
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(target.exists())

    def test_aggregate_and_child_cannot_be_selected_together(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp) / 'profile'
            result = self.invoke(target, '--plugins', '@neystan/dsh-web-ui-all', '@neystan/dsh-pet', '--apply')
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(target.exists())

if __name__ == '__main__':
    unittest.main()
