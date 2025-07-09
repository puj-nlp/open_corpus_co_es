# Open Corpus CO-ES

Sistema de descarga y carga de corpus en español, con enfoque en Colombia y América Latina, para tareas de procesamiento de lenguaje natural (PLN).

## Características

- 📥 **Descarga automatizada** desde Google Drive (mediante `gdown` o URL directa)
- 🧾 **Catálogo ** con metadatos de más de 70 corpus y recursos léxicos
- 📚 **Carga flexible** de corpus en múltiples formatos
- 🧪 **Pruebas automáticas** de carga para todos los corpus activos
- 🧰 **Línea de comandos** y uso como módulo de Python

---

## Estructura del Proyecto

```
open_corpus_co_es/
├── downloader.py         # Descarga y validación de archivos
├── loader.py             # Carga de corpus según su formato
├── utils.py              # Ruta local para almacenamiento 
├── demo.py               # Script de prueba para un solo corpus
├── demo_all.py           # Script de prueba para todos los corpus
├── test_loader.py        # Test unitarios
├── __main__.py           # Entrada desde CLI
```

---

## ▶Instalación

### Desde Pip

```bash
pip install open_corpus_co_es
```

---

## Uso Básico

### Listar corpus disponibles

```bash
python -m open_corpus_co_es --list
```

### Descargar un corpus

```bash
python -m open_corpus_co_es --download salud_colombia_2024_v2
```

### Descargar forzando reescritura

```bash
python -m open_corpus_co_es --download salud_colombia_2024_v2 --force
```

### Descargar todos los corpus habilitados

```bash
python -m open_corpus_co_es --download_all
```

### Ejecutar pruebas automáticas

```bash
python -m open_corpus_co_es.test_loader
```

## Funciones Clave

### `download_corpus(name: str, force=False)`
Descarga un corpus especificado por `name` usando su ID de Google Drive o URL. Verifica estructura básica y formatos.

### `load_corpus(name: str)`
Carga un corpus previamente descargado. Aplica extracción automática de texto desde diferentes formatos.

### `list_corpus()`
Retorna metadatos del catálogo activo en forma de diccionario.

---


Puedes acceder directamente a los archivos procesados para análisis posterior.

---

## Ejemplo de Uso en Python

```python
from open_corpus_co_es.loader import load_corpus, list_corpus
from open_corpus_co_es.downloader import download_corpus

print(f"Corpus disponibles: {list_corpus()}")
nombre = "presidentes"

print(f"\n📥 Descargando y cargando corpus: {nombre}")
download_corpus(nombre, force=True)
datos = load_corpus(nombre)
print("\n✅ Corpus cargado correctamente\n")
print(f"\n📄 Primer documento: {datos[:1]}")
```

---

## Prueba interactiva

```bash
python demo.py --corpus presindetes
```

---

## Autor y Créditos

**Luis Gabriel Moreno Sandoval**  
Pontificia Universidad Javeriana  
morenoluis@javeriana.edu.co

## Licencia

MIT License