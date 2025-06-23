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
    for name in list_corpus().keys():
        print(" -", name)
    # Error:
    #  - educacion_argentina_2024_v2
    #  - educacion_argentina_2024_v1
    #  - educacion_colombia_2024_v2
    #  - educacion_colombia_2024_v1
    #  - educacion_mexico_2024_v2
    #  - educacion_mexico_2024_v1
    #  - salud_argentina_2024_v2
    #  - salud_argentina_2024_v1
    #  - salud_colombia_2024_v1
    #  - salud_colombia_2024_v2
    #  - salud_mexico_2024_v1
    #  - salud_mexico_2024_v2
    #  - seguridad_argentina_2024_v2
    #  - seguridad_argentina_2024_v1
    #  - seguridad_colombia_2024_v2
    #  - seguridad_colombia_2024_v1
    #  - seguridad_mexico_2024_v2
    #  - seguridad_mexico_2024_v1
    # "entrevistas_victimas_publicas" "edades"
    # "es_hs_pject_raw_extended"
    # "ods", "laudato_si"

    # list_corpus = ["presidentes", "dataset_bancos_2022", "perfiles_periodistas_2020", "tweets_miscelaneos_2020"]
    # list_corpus = ["news_2020_peru_v2", "news_2020_colombia_v2", "news_2020_ecuador_v2"]
    # list_corpus = ["musica", "educacion_primaria"]
    # list_corpus = ["llm_humano", "discurso_odio"]
    # list_corpus = [
    #     "consolidated_anew_xanew_ncr_inquirer_sel_spanish",
    #     # "lexicon_tic",
    #     "lexicon_actors_roles",
    #     "lexicon_afectivo_categorias",
    #     "lexicon_afectivo_categorias_v2",
    #     "lexicon_duelo_completa",
    #     "lexicon_ejecuciones_extrajudiciales",
    #     "lexicon_estigmatización",
    #     # "lexicon_ministers",
    #     "lexicon_ministers_v2",
    #     "lexicon_referencia_crea",
    #     "lexicon_referencia_creav_2",
    #     # "lexicon_relations_verbs",
    #     # "lexicon_relations_verbs_v2",
    #     # "lexicon_sevicia",
    #     # "lexicon_verbos_sentencias_tierras",
    #     # "lexicon_verbos_sentencias_tierras_v2",
    #     "tesauro_cev"
    # ]

    #list_corpus = ["lexicon_referencia_crea", "tesauro_cev"]

    list_corpus = ["presidentes", "laudato_si", "corpus_new", "musica"]

    for name in list_corpus:
        try:
            download_corpus(name)
            corpus = load_corpus(name)
            mostrar_preview(name, corpus)
        except Exception as e:
            print(f"❌ Error al cargar el corpus '{name}': {e}")
