import os
import json
import requests
import logging
import importlib.resources
from tqdm import tqdm
from zipfile import ZipFile, is_zipfile as is_zipfile_local
from .utils import ensure_data_dir
import gdown

# Configurar logger
logger = logging.getLogger("corpus_downloader")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def load_catalog():
    with importlib.resources.open_text("open_corpus_co_es", "catalog_v2.json", encoding="utf-8") as f:
        raw = json.load(f)

    catalog = {}
    enabled_map = {}

    for entry in raw:
        key = os.path.splitext(entry["archivo"])[0]
        enabled = entry.get("enabled", True)
        entry["enabled"] = enabled
        catalog[key] = entry
        enabled_map[key] = enabled

    return catalog, enabled_map

CATALOG, CATALOG_ENABLED = load_catalog()

def get_corpus_path(name):
    return os.path.join(ensure_data_dir(), name)

def validate_corpus_structure(corpus_dir, expected_subfolder=None):
    """
    Verifica si el corpus contiene archivos válidos luego de la descarga y extracción.
    """
    path_to_check = os.path.join(corpus_dir, expected_subfolder) if expected_subfolder else corpus_dir
    if not os.path.exists(path_to_check):
        raise FileNotFoundError(f"[ERROR] No se encontró el directorio esperado: {path_to_check}")

    valid_extensions = [".txt", ".json", ".csv", ".xml", ".html", ".rdf"]
    found_valid_file = False

    for root, dirs, files in os.walk(path_to_check):
        for file in files:
            if any(file.endswith(ext) for ext in valid_extensions):
                found_valid_file = True
                break
        if found_valid_file:
            break

    if not found_valid_file:
        raise Exception(f"[ERROR] No se encontraron archivos válidos en {path_to_check}. "
                        f"Verifica que el archivo ZIP esté bien estructurado.")

    logger.info(f"✅ Estructura de corpus o recurso válida en: {path_to_check}")

def download_corpus_old(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus o Recurso '{name}' no está disponible en el catálogo. Por favor, revisa el nombre.")

    if not CATALOG_ENABLED[name]:
        raise Exception(f"Corpus o Recurso '{name}' no está habilitado en el catálogo.")

    corpus_dir = get_corpus_path(name)

    if os.path.exists(corpus_dir) and os.listdir(corpus_dir):
        if not force:
            logger.info(f"[INFO] Corpus '{name}' ya está cargado. Usa force=True para forzar descarga.")
            return
        else:
            logger.info(f"[INFO] Reescribiendo corpus '{name}'...")
            import shutil
            shutil.rmtree(corpus_dir)

    os.makedirs(corpus_dir, exist_ok=True)
    url = CATALOG[name].get("url_descarga")
    if not url:
        raise ValueError(f"Corpus '{name}' no tiene una URL de descarga válida.")

    logger.info(f"⬇️ Cargando corpus '{name}' ...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        logger.error(f"Error HTTP al descargar el corpus '{name}': status {response.status_code}")
        raise Exception(f"No se pudo cargar el archivo '{name}' (status {response.status_code}).")

    tmp_path = os.path.join(corpus_dir, "tmp_download")
    logger.debug(f"[TMP] Guardando archivo temporal en {tmp_path}")

    with open(tmp_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

    if is_zipfile_local(tmp_path):
        logger.info("📦 Archivo ZIP detectado. Iniciando descompresión...")
        try:
            with ZipFile(tmp_path, "r") as zip_ref:
                zip_ref.extractall(corpus_dir)
            os.remove(tmp_path)
            logger.info("✔️ Descompresión completada correctamente.")
        except Exception as e:
            logger.exception(f"[ERROR] Falló la descompresión del ZIP: {e}")
            raise

        subfolder = CATALOG[name].get("subfolder")
        if subfolder:
            subfolder_path = os.path.join(corpus_dir, subfolder)
            if not os.path.exists(subfolder_path):
                raise FileNotFoundError(
                    f"[ERROR] Se esperaba la subcarpeta '{subfolder}' dentro del corpus '{name}', pero no se encontró."
                )
        else:
            logger.info(f"[INFO] No se especificó subcarpeta. Archivos extraídos directamente en {corpus_dir}.")
    else:
        ext = CATALOG[name].get("extension", "txt")
        final_path = os.path.join(corpus_dir, f"{name}.{ext}")
        os.rename(tmp_path, final_path)
        logger.info(f"🔄 Archivo no ZIP detectado. Guardado como: {final_path}")

    # Validar estructura del corpus
    validate_corpus_structure(corpus_dir, subfolder if is_zipfile_local(tmp_path) and CATALOG[name].get("subfolder") else None)

    logger.info(f"✅ Corpus '{name}' listo en: {corpus_dir}")

def download_corpus_old_old(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")

    if not CATALOG_ENABLED[name]:
        raise Exception(f"Corpus '{name}' no está habilitado.")

    path = get_corpus_path(name)

    if os.path.exists(path) and os.listdir(path):
        if not force:
            logger.info(f"Corpus '{name}' ya descargado. Usa force=True para reescribir.")
            return
        import shutil
        shutil.rmtree(path)

    os.makedirs(path, exist_ok=True)
    url = CATALOG[name].get("url_descarga")
    if not url:
        raise ValueError(f"El corpus '{name}' no tiene una URL de descarga válida.")

    logger.info(f"⬇️ Cargando corpus '{name}'...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"No se pudo descargar el corpus (status {response.status_code})")

    tmp_path = os.path.join(path, "tmp_download")
    with open(tmp_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

    if is_zipfile_local(tmp_path):
        logger.info("📦 ZIP detectado. Descomprimiendo...")
        with ZipFile(tmp_path, "r") as zip_ref:
            zip_ref.extractall(path)
        os.remove(tmp_path)
        logger.info("✔️ Descompresión completada correctamente.")
        logger.info(f"[INFO] No se especificó subcarpeta. Archivos extraídos directamente en {path}.")
        validate_corpus_structure(path)
    else:
        ext = CATALOG[name].get("extension", "txt").lower()
        final_path = os.path.join(path, f"{name}.{ext}")
        os.rename(tmp_path, final_path)
        logger.info(f"🔄 Archivo no ZIP detectado. Guardado como: {final_path}")

        # Si es un archivo plano (parquet, xlsx, etc.), omitimos validación estructural de carpeta
        extensiones_planas_validas = {"parquet", "xlsx", "json", "jsonl", "csv"}
        if ext in extensiones_planas_validas:
            logger.info(f"Omitiendo validación de estructura para archivo plano '{ext}'.")
            return
        else:
            validate_corpus_structure(final_path)

    logger.info(f"✅ Corpus '{name}' listo en: {path}")

def download_corpus(name, force=False):
    if name not in CATALOG:
        raise ValueError(f"Corpus '{name}' no está en el catálogo.")

    if not CATALOG_ENABLED[name]:
        raise Exception(f"Corpus '{name}' no está habilitado.")

    path = get_corpus_path(name)

    if os.path.exists(path) and os.listdir(path):
        if not force:
            logger.info(f"Corpus '{name}' ya descargado. Usa force=True para reescribir.")
            return
        import shutil
        shutil.rmtree(path)

    os.makedirs(path, exist_ok=True)

    url = CATALOG[name].get("url_descarga")
    file_id = CATALOG[name].get("id")
    ext = CATALOG[name].get("extension", "txt").lower()
    tmp_path = os.path.join(path, "tmp_download")
    final_path = os.path.join(path, f"{name}.{ext}")

    if not url and not file_id:
        raise ValueError(f"El corpus '{name}' no tiene una URL de descarga ni un ID de Google Drive válido.")

    logger.info(f"⬇️ Cargando corpus '{name}'...")

    try:
        # Modo GDOWN si el archivo es de Google Drive con ID
        if file_id:
            gdown.download(id=file_id, output=final_path, quiet=False)
        else:
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                raise Exception(f"No se pudo descargar el corpus (status {response.status_code})")

            with open(tmp_path, "wb") as f:
                for chunk in tqdm(response.iter_content(chunk_size=8192)):
                    if chunk:
                        f.write(chunk)

            if is_zipfile_local(tmp_path):
                logger.info("📦 ZIP detectado. Descomprimiendo...")
                with ZipFile(tmp_path, "r") as zip_ref:
                    zip_ref.extractall(path)
                os.remove(tmp_path)
                logger.info("✔️ Descompresión completada correctamente.")
                logger.info(f"[INFO] No se especificó subcarpeta. Archivos extraídos directamente en {path}.")
                validate_corpus_structure(path)
                return
            else:
                os.rename(tmp_path, final_path)
                logger.info(f"🔄 Archivo no ZIP detectado. Guardado como: {final_path}")
    except Exception as e:
        logger.error(f"❌ Error al descargar el corpus '{name}': {e}")
        raise

    # Validar si es archivo plano
    extensiones_planas_validas = {"parquet", "xlsx", "json", "jsonl", "csv"}
    if ext in extensiones_planas_validas:
        logger.info(f"✔️ Archivo plano '{ext}' descargado correctamente. Omitiendo validación de estructura de carpeta.")
        return
    else:
        validate_corpus_structure(final_path)

    logger.info(f"✅ Corpus '{name}' listo en: {path}")

def download_all_corpus(force=False):
    for name in CATALOG:
        try:
            logger.info(f"\n📥 Probando corpus: {name}")
            download_corpus(name, force=force)
        except Exception as e:
            logger.error(f"❌ Error con corpus '{name}': {e}")
