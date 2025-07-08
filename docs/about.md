---
title: Librería y Créditos
---
---
layout: page
title: Créditos y Librería
permalink: /about/
nav_order: 1
---

## Créditos

Proyecto desarrollado por **Luis Gabriel Moreno Sandoval** y colaboradores.

## Librería

La librería `open_corpus_co_es` permite acceder de forma sencilla a conjuntos de datos textuales en español con énfasis en contextos latinoamericanos.

Puedes usarla desde la terminal:

```bash
python -m open_corpus_co_es --list
python -m open_corpus_co_es --download <nombre_del_corpus>
```

O desde Python:

```python
from open_corpus_co_es import load_corpus
df = load_corpus("nombre_del_corpus")
```

## 📁 Estructura del Código

```
open_corpus_co_es/
├── downloader.py         # Descarga archivos desde Google Drive o URL
├── loader.py             # Carga automática según tipo de archivo
├── utils.py              # Ruta local (~/.open_corpus_co_es/data)
├── catalog.json          # Metadatos de los corpus
├── demo.py               # Prueba de un corpus
├── test_loader.py        # Pruebas automatizadas
├── __main__.py           # CLI
```

## 🔧 Ejemplo de uso en Python

```python
from open_corpus_co_es.loader import load_corpus
docs = load_corpus("salud_colombia_2024_v2")
print(docs[0]['text'])
```

## 👨‍💻 Autor y Créditos

**Luis Gabriel Moreno Sandoval**  
Pontificia Universidad Javeriana  
📧 morenoluis@javeriana.edu.co

Con el apoyo del grupo de investigación en Procesamiento de Lenguaje Natural (PUJ-NLP).

## 🧾 Licencia

MIT License