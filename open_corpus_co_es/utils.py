import os

def ensure_data_dir():
    """
    Crea (si no existe) y retorna la ruta al directorio de datos local donde se guardan los corpus.
    Por defecto: ~/.open_corpus_co_es/data
    """
    base_dir = os.path.expanduser("~/.open_corpus_co_es/data")
    os.makedirs(base_dir, exist_ok=True)
    return base_dir
