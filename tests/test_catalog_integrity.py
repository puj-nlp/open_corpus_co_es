import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from open_corpus_co_es import downloader
from open_corpus_co_es.loader import extract_documents_from_dataframe, extract_text_from_file


class TestCatalogIntegrity(unittest.TestCase):
    def test_every_entry_has_unique_name_and_verified_metadata(self):
        resource = Path(__file__).parents[1] / "open_corpus_co_es" / "catalog.json"
        entries = json.loads(resource.read_text(encoding="utf-8"))
        names = [entry.get("nombre", Path(entry["archivo"]).stem) for entry in entries]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(names), len(downloader.CATALOG))
        for entry in entries:
            with self.subTest(name=entry["archivo"]):
                self.assertEqual(Path(entry["archivo"]).suffix, "." + entry["extension"])
                self.assertGreater(entry["filas"], 0)
                self.assertGreater(entry["bytes"], 0)
                self.assertEqual(len(entry["sha256"]), 64)
                self.assertEqual(entry["columnas"], len(entry["campos"]))
                if entry.get("columna_texto"):
                    self.assertIn(entry["columna_texto"], entry["campos"])

    def test_excel_variants_do_not_hide_parquet(self):
        for name in ("educacion_primaria", "llm_humano"):
            self.assertEqual(downloader.CATALOG[name]["extension"], "parquet")
            self.assertEqual(downloader.CATALOG[name + "_excel"]["extension"], "xlsx")

    def test_exact_text_column_precedes_text_hash(self):
        frame = pd.DataFrame([{"text_sha256": "hash", "text": "Texto original"}])
        self.assertEqual(extract_documents_from_dataframe(frame)[0]["text"], "Texto original")

    def test_hit_sentence_precedes_empty_opening_text(self):
        frame = pd.DataFrame([{"Opening Text": None, "Hit Sentence": "Publicación original"}])
        self.assertEqual(extract_documents_from_dataframe(frame)[0]["text"], "Publicación original")

    def test_headerless_csv_preserves_first_record(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "crea.csv"
            path.write_text("de;9999518;6554555\nla;6277560;4114859\n", encoding="utf-8")
            metadata = {"columna_texto": "word", "opciones_lectura": {"header": None, "names": ["word", "freq", "norm"]}}
            documents = extract_text_from_file(str(path), metadata)
            self.assertEqual(len(documents), 2)
            self.assertEqual(documents[0]["text"], "de")

    def test_empty_text_rows_keep_metadata(self):
        frame = pd.DataFrame([{"id": 1, "text": ""}, {"id": 2, "text": None}])
        documents = extract_documents_from_dataframe(frame)
        self.assertEqual(documents, [{"text": "", "id": 1}, {"text": "", "id": 2}])

    def test_json_array_is_loaded_as_documents(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "documents.json"
            path.write_text('[{"text": "Uno"}, {"text": "Dos"}]', encoding="utf-8")
            self.assertEqual(len(extract_text_from_file(str(path))), 2)

    def test_failed_force_download_keeps_previous_file(self):
        name = "presidentes"
        metadata = {"extension": "parquet", "id": "test-id", "bytes": 8,
                    "sha256": hashlib.sha256(b"original").hexdigest()}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / (name + ".parquet")
            path.write_bytes(b"original")

            def corrupt_download(id, output, quiet, use_cookies):
                Path(output).write_bytes(b"corrupt!")
                return output

            with patch.dict(downloader.CATALOG, {name: metadata}), \
                    patch.object(downloader, "get_corpus_path", return_value=directory), \
                    patch.object(downloader.gdown, "download", side_effect=corrupt_download):
                with self.assertRaises(ValueError):
                    downloader.download_corpus(name, force=True)
            self.assertEqual(path.read_bytes(), b"original")
            self.assertFalse((Path(directory) / ".tmp_download").exists())

    def test_download_all_skips_disabled_entries(self):
        with patch.object(downloader, "CATALOG", {"active": {}, "disabled": {}}), \
                patch.object(downloader, "CATALOG_ENABLED", {"active": True, "disabled": False}), \
                patch.object(downloader, "download_corpus") as download:
            self.assertEqual(downloader.download_all_corpus(), {})
            download.assert_called_once_with("active", force=False)

    def test_crea_preserves_literal_nan_and_null(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "crea.csv"
            path.write_text("nan;40;26\nnull;5;3\n", encoding="utf-8")
            metadata = downloader.CATALOG["lexicon_referencia_crea"]
            documents = extract_text_from_file(str(path), metadata)
            self.assertEqual([document["text"] for document in documents], ["nan", "null"])
