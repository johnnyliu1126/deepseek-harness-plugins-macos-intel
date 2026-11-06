import base64
import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'collection.py'
spec = importlib.util.spec_from_file_location('collection_installer', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class Response(io.BytesIO):
    def __init__(self, body, length):
        super().__init__(body)
        self.headers = {'Content-Length': str(length)}

class DownloadTest(unittest.TestCase):
    def test_incomplete_response_is_identified_before_hash_acceptance(self):
        data = b'partial'
        integrity = 'sha512-' + base64.b64encode(hashlib.sha512(data).digest()).decode()
        with tempfile.TemporaryDirectory() as tmp, patch.object(module.urllib.request, 'urlopen', return_value=Response(data, 999)):
            with self.assertRaisesRegex(ValueError, 'Incomplete download'):
                module.download_verified('https://example.org/plugin.tgz', integrity, Path(tmp) / 'plugin.tgz')

    def test_full_length_with_wrong_integrity_is_rejected(self):
        data = b'archive bytes'
        integrity = 'sha512-' + base64.b64encode(hashlib.sha512(b'different').digest()).decode()
        with tempfile.TemporaryDirectory() as tmp, patch.object(module.urllib.request, 'urlopen', return_value=Response(data, len(data))):
            with self.assertRaisesRegex(ValueError, 'Integrity mismatch'):
                module.download_verified('https://example.org/plugin.tgz', integrity, Path(tmp) / 'plugin.tgz')

if __name__ == '__main__':
    unittest.main()
