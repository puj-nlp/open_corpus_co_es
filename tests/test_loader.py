import unittest
from open_corpus_co_es import list_corpus, load_corpus
from open_corpus_co_es.downloader import download_corpus

class TestCorpusLoader(unittest.TestCase):

    def test_list_corpus(self):
        corpus_list = list_corpus()
        self.assertIn("presidentes", corpus_list)

    def test_download_and_load(self):
        download_corpus("presidentes")
        corpus = load_corpus("presidentes")
        self.assertIsNotNone(corpus)
        self.assertGreater(len(corpus), 10)  # Debe tener al menos 10 tokens

if __name__ == "__main__":
    unittest.main()
