# Open Corpus CO-ES

Este componente proporciona acceso automatizado a un conjunto de corpus de prueba para tareas de NLP en español. Permite su descarga, carga y visualización desde scripts en Python o la línea de comandos.

## 📁 Estructura del Proyecto

```
open_corpus_co_es/
├── downloader.py         # Descarga y extracción de archivos
├── loader.py             # Carga según tipo de archivo (texto, CSV, RDF, etc.)
├── utils.py              # Gestión de rutas locales
├── catalog_v2.json       # Catálogo de corpus disponibles
├── demo.py               # Carga interactiva de un corpus
├── demo_all.py           # Pruebas sobre todos los corpus activos
├── test_loader.py        # Pruebas básicas de carga para todos los corpus
├── __main__.py           # Punto de entrada CLI para el módulo
```

## ▶️ Requisitos

```bash
pip install -r requirements.txt
```

## 📦 Instalación

Puedes instalar el componente directamente desde GitHub usando `pip`:

```bash
pip install git+https://github.com/puj-nlp/open_corpus_co_es.git
```

O si usas la conexión SSH:

```bash
pip install git+ssh://git@github.com:puj-nlp/open_corpus_co_es.git
```

Esto instalará la librería como un módulo que puedes usar desde Python o desde la línea de comandos con:

```bash
python -m open_corpus_co_es --list
```

## 🚀 Uso Básico

### Desde los scripts de demostración:

#### Ver todos los corpus disponibles:
```bash
python demo.py --listar
```

#### Descargar y cargar un corpus:
```bash
python demo.py --corpus presidente
```

#### Probar todos los corpus habilitados:
```bash
python demo_all.py
```

### Desde la línea de comandos con `-m`:

#### Ver todos los corpus disponibles:
```bash
python -m open_corpus_co_es --list
```

#### Descargar un corpus específico:
```bash
python -m open_corpus_co_es --download presidente
```

#### Descargar forzando sobreescritura:
```bash
python -m open_corpus_co_es --download presidente --force
```

#### Descargar todos los corpus:
```bash
python -m open_corpus_co_es --download_all
```

### Desde la terminal como comando (requiere instalación previa con setup.py):

#### Ver corpus disponibles:
```bash
open-corpus --list
```

#### Descargar un corpus:
```bash
open-corpus --download presidente
```

### Ejecutar pruebas automáticas:
```bash
python -m open_corpus_co_es.test_loader
```

## 📦 Tipos de archivos soportados
- `.csv`, `.tsv` (se detecta automáticamente el separador)
- `.xlsx`, `.parquet`
- `.txt`
- `.rdf` (ontologías)
- `.json`, `.jsonl`

## 📘 Notas
- Todos los corpus se almacenan localmente en `~/.open_corpus_co_es/data/`
- El sistema reconoce y procesa los formatos automáticamente.
- Puedes usar el parámetro `--force` para forzar la re-descarga.

## ✅ Licencia
MIT License