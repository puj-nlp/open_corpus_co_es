---
title: Librería y Créditos
---

# 📦 Librería: open_corpus_co_es

Este proyecto facilita el acceso a múltiples corpus curados en español para tareas de NLP. Incluye un sistema de descarga, carga automática según tipo de archivo, y procesamiento básico de los textos.

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