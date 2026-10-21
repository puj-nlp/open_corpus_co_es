import unittest
from unittest.mock import patch

from open_corpus_co_es.__main__ import main


class TestCLI(unittest.TestCase):
    def test_force_is_forwarded(self):
        with patch("sys.argv", ["open_corpus_co_es", "--download", "presidentes", "--force"]), \
                patch("open_corpus_co_es.__main__.download_corpus") as download, \
                patch("builtins.print"):
            main()
            download.assert_called_once_with("presidentes", force=True)

    def test_download_failure_exits_with_error(self):
        with patch("sys.argv", ["open_corpus_co_es", "--download", "missing"]), \
                patch("open_corpus_co_es.__main__.download_corpus", side_effect=ValueError("missing")), \
                patch("builtins.print"), patch("sys.stderr"):
            with self.assertRaises(SystemExit) as result:
                main()
            self.assertEqual(result.exception.code, 1)

    def test_download_all_reports_failures(self):
        with patch("sys.argv", ["open_corpus_co_es", "--download_all"]), \
                patch("open_corpus_co_es.__main__.download_all_corpus", return_value={"missing": "error"}), \
                patch("sys.stderr"):
            with self.assertRaises(SystemExit) as result:
                main()
            self.assertEqual(result.exception.code, 1)
