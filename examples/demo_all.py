from open_corpus_co_es import list_corpus, load_corpus
from open_corpus_co_es.downloader import download_corpus

def mostrar_preview(nombre, corpus):
    print(f"\n📘 Corpus: {nombre}")
    if isinstance(corpus, dict):
        print(f"🔹 Total documentos: {len(corpus)}")
        for i, (k, v) in enumerate(corpus.items()):
            print(f"  - Documento: {k}")
            print(f"    Contenido: {v[:150]}...")
            if i >= 1:
                break
    elif isinstance(corpus, list):
        print(f"🔹 Total registros: {len(corpus)}")
        print("🔍 Ejemplo del primero:")
        print(corpus[0] if corpus else "[VACÍO]")
    else:
        print(f"🔹 Total tokens: {len(corpus)}")
        print("🔍 Primeros tokens:")
        print(corpus[:20])

if __name__ == "__main__":
    print("📚 Corpus disponibles:")
    catalog = list_corpus()
    for name in catalog.keys():
        print(" -", name)
    count = 0
    for name in catalog.keys():
        count += 1
        if count > 5:
            print("⚠️ Solo mostrando los primeros 5 corpus.")
            break
        try:
            print(f"\n⬇️ Descargando corpus: {name}...")
            download_corpus(name)
            corpus = load_corpus(name)
            mostrar_preview(name, corpus)
        except Exception as e:
            print(f"⚠️ Error al procesar '{name}': {e}")
