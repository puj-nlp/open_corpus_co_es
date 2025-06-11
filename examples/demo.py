from open_corpus_co_es import list_corpus, load_corpus
from open_corpus_co_es.downloader import download_corpus

print("Corpus disponibles:")
print(list_corpus())

download_corpus("presidentes")
corpus = load_corpus("presidentes")
print("Primeras palabras del corpus:", corpus[:20])

download_corpus("dataset_bancos_2022")
corpus = load_corpus("dataset_bancos_2022")
print("Primeras palabras del corpus:", corpus[:20])