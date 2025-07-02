# test_loader.py
import unittest
from open_corpus_co_es.loader import load_corpus, list_corpus
from open_corpus_co_es.downloader import download_corpus

class TestCorpusLoader(unittest.TestCase):

    def test_list_corpus_structure(self):
        catalog = list_corpus()
        self.assertIsInstance(catalog, dict)
        for name, metadata in catalog.items():
            self.assertNotIn("archivo", metadata)
            self.assertNotIn("url", metadata)
            self.assertNotIn("id", metadata)
            self.assertNotIn("url_descarga", metadata)
            self.assertIn("descripcion", metadata)

    def test_download_and_load_by_extension(self):
        # Uno por tipo de archivo
        selected = [
            "presidentes",                        # zip -> txt
            "dataset_bancos_2022",               # parquet con Raw_data no válido
            "lexicon_sevicia",       # csv
            "lexicon_afectivo_categorias_v2",    # xlsx
            "news_2020_peru_v2"
        ]
        for name in selected:
            with self.subTest(name=name):
                download_corpus(name)
                try:
                    corpus = load_corpus(name)
                    self.assertIsNotNone(corpus)
                    self.assertGreater(len(corpus), 1)
                    self.assertTrue(all(isinstance(token, dict) for token in corpus))
                except Exception as e:
                    self.fail(f"Fallo al cargar corpus '{name}': {e}")

