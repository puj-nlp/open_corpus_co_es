import argparse
from open_corpus_co_es.loader import load_corpus, list_corpus
from open_corpus_co_es.downloader import download_corpus
import pprint

def mostrar_corpus(nombre):
    try:
        print(f"\n📥 Descargando y cargando corpus: {nombre}")
        download_corpus(nombre)
        datos = load_corpus(nombre)
        print("\n✅ Corpus cargado correctamente\n")

        if isinstance(datos, dict):
            print(f"🔍 Corpus tipo diccionario con {len(datos)} entradas")
            for k in list(datos.keys())[:3]:
                print(f"- {k} → {str(datos[k])[:100]}...")

        elif isinstance(datos, list):
            print(f"📚 Lista de {len(datos)} documentos. Ejemplo:")
            pprint.pprint(datos[0], indent=2, width=100)

        elif hasattr(datos, 'serialize'):
            print("📘 RDF Graph detectado. Número de triples:", len(datos))
            print("Triples ejemplo:")
            for s, p, o in list(datos)[:5]:
                print(f"  - {s} {p} {o}")

        else:
            print("📝 Texto plano:")
            print(str(datos)[:500])

    except Exception as e:
        print(f"❌ Error cargando el corpus '{nombre}': {e}")


def main(corpus=None):
    parser = argparse.ArgumentParser(description="Demo para probar carga de corpus")
    parser.add_argument("--corpus", help="Nombre del corpus a cargar (usa --listar para ver disponibles)")
    parser.add_argument("--listar", action="store_true", help="Listar corpus disponibles")
    args = parser.parse_args()

    if args.listar:
        print("\n📂 Corpus disponibles:")
        for nombre in list_corpus():
            print(f"- {nombre}")
        return
    elif corpus:
        print("\n📂 Corpus disponibles:")
        for nombre in list_corpus():
            print(f"- {nombre}")

    if corpus:
        mostrar_corpus(corpus)
    elif args.corpus:
        mostrar_corpus(args.corpus)
    else:
        print("❗ Por favor, indica un corpus con --corpus o usa --listar para ver las opciones.")


if __name__ == "__main__":
    main("rag_processed_data")
