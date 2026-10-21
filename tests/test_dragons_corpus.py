import shutil
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pyarrow as pa
import pyarrow.parquet as pq

from open_corpus_co_es.downloader import CATALOG, download_corpus
from open_corpus_co_es.loader import list_corpus, load_corpus


class TestDragonsCorpus(unittest.TestCase):
    corpus_name = "dragons_rag_2026_10_19"

    def test_catalog_metadata(self):
        metadata = list_corpus()[self.corpus_name]
        self.assertEqual(metadata["extension"], "parquet")
        self.assertEqual(metadata["documentos"], 169248)
        self.assertEqual(sum(metadata["fuentes"].values()), metadata["documentos"])
        self.assertEqual(len(metadata["sha256"]), 64)
        self.assertTrue(metadata["enabled"])
        self.assertEqual(CATALOG[self.corpus_name]["id"], "1JN8PhSXiUoeE45bBDOpfNyvNicLO2GQn")

    def test_download_load_and_force_with_nested_metadata(self):
        records = [
            {
                "document_id": "document-1",
                "text": "Texto original con tildes: educación.\nSegunda línea.",
                "source": "bluesky",
                "keyword_matches": ["educación", "Colombia"],
                "top_terms": [{"term": "educación", "count": 2}],
                "title": None,
            },
            {
                "document_id": "document-2",
                "text": "Otro documento.",
                "source": "media_cloud",
                "keyword_matches": [],
                "top_terms": [],
                "title": "Título",
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            fixture_path = Path(directory) / "fixture.parquet"
            corpus_path = Path(directory) / self.corpus_name
            pq.write_table(pa.Table.from_pylist(records), fixture_path)
            fixture_metadata = dict(CATALOG[self.corpus_name])
            fixture_metadata["bytes"] = fixture_path.stat().st_size
            fixture_metadata["sha256"] = hashlib.sha256(fixture_path.read_bytes()).hexdigest()

            def copy_fixture(id, output, quiet, use_cookies):
                shutil.copyfile(fixture_path, output)
                return output

            with patch.dict(CATALOG, {self.corpus_name: fixture_metadata}), \
                    patch("open_corpus_co_es.downloader.get_corpus_path", return_value=str(corpus_path)), \
                    patch("open_corpus_co_es.loader.get_corpus_path", return_value=str(corpus_path)), \
                    patch("open_corpus_co_es.downloader.gdown.download", side_effect=copy_fixture) as download:
                download_corpus(self.corpus_name)
                documents = load_corpus(self.corpus_name)
                self.assertEqual(len(documents), 2)
                self.assertEqual(documents[0]["text"], records[0]["text"])
                self.assertEqual(documents[0]["document_id"], "document-1")
                self.assertEqual(list(documents[0]["keyword_matches"]), records[0]["keyword_matches"])
                self.assertEqual(list(documents[0]["top_terms"]), records[0]["top_terms"])
                self.assertEqual(list(documents[1]["keyword_matches"]), [])
                self.assertNotIn("title", documents[0])
                download.assert_called_once_with(
                    id=CATALOG[self.corpus_name]["id"],
                    output=str(corpus_path / ".tmp_download"),
                    quiet=True,
                    use_cookies=False,
                )
                download_corpus(self.corpus_name)
                self.assertEqual(download.call_count, 1)
                download_corpus(self.corpus_name, force=True)
                self.assertEqual(download.call_count, 2)
                self.assertEqual(len(load_corpus(self.corpus_name)), 2)
