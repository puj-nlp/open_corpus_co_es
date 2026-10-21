---
layout: page
title: Publicación
permalink: /publicacion/
nav_order: 5
---

# Publicación de Open Corpus CO-ES

La versión **[0.1.1a4](https://pypi.org/project/open-corpus-co-es/0.1.1a4/)** fue publicada
y verificada el **21 de octubre de 2026**. Es una versión preliminar. La versión se define
en `pyproject.toml`; `setup.py` utiliza esa configuración para evitar divergencias.
El catálogo forma parte del wheel y la distribución fuente. Los corpus permanecen
en Drive. La distribución fuente también incluye documentación y scripts de auditoría.

## Antes de construir

Para reproducir exactamente la versión publicada, utiliza su distribución fuente
disponible en [PyPI](https://pypi.org/project/open-corpus-co-es/0.1.1a4/#files).
Los comandos de esta sección se ejecutan desde la carpeta de esa distribución.

```bash
pip install -e ".[dev]"
python -m pytest tests
python scripts/audit_corpora.py --root "H:\Unidades compartidas\Corpus"
python scripts/verify_downloads.py
python scripts/verify_loaders.py "H:\Unidades compartidas\Corpus"
```

`audit_corpora.py` inspecciona los archivos tabulares locales y reporta errores sin
alterar los datos. Puede encontrar archivos fuera del catálogo; estos se evalúan
por separado. `verify_downloads.py` comprueba todas las entradas habilitadas sin
cookies, y compara el tamaño y SHA-256. `verify_loaders.py` carga todas las entradas
del inventario y contrasta la cantidad de registros, incluida la entrada deshabilitada
que se inspecciona localmente. Los informes se escriben en `temp/`.

La auditoría técnica no acredita por sí sola la exactitud histórica, la autoría,
las licencias ni la cobertura documental de las fuentes. Consulta las limitaciones
del [informe de auditoría]({{ '/auditoria/' | relative_url }}).

## Construcción y comprobación

```bash
python -m build
python -m twine check --strict dist/open_corpus_co_es-0.1.1a4-py3-none-any.whl dist/open_corpus_co_es-0.1.1a4.tar.gz
```

Comprueba que ambos artefactos contienen el catálogo de 66 entradas y que el wheel
no contiene parquet ni archivos de configuración local. La autenticación se configura
con un token de PyPI limitado al proyecto en el gestor de credenciales de Twine,
el archivo personal `.pypirc` o la variable de entorno `TWINE_PASSWORD`; el usuario
de autenticación por token es `__token__`.

Twine no carga automáticamente archivos `.env`: las variables deben estar disponibles
en el entorno del proceso. Las credenciales personales no forman parte de los archivos
publicados ni de la documentación del sitio.

## Subida a PyPI

```bash
python -m twine upload --non-interactive dist/open_corpus_co_es-0.1.1a4-py3-none-any.whl dist/open_corpus_co_es-0.1.1a4.tar.gz
```

Se especifican los dos archivos exactos para no volver a subir versiones antiguas
que puedan estar en `dist/`. PyPI no permite reemplazar una distribución publicada
con el mismo nombre y versión. Si cambian los artefactos después de publicarlos,
se debe preparar otra versión.

**Esta versión ya está publicada:** los comandos anteriores documentan el procedimiento
utilizado. Para una publicación futura, cambia la versión y los nombres de los artefactos.

## Verificación posterior

Confirma la presencia de ambos artefactos en la
[ficha de PyPI](https://pypi.org/project/open-corpus-co-es/) y compara sus SHA-256
con los archivos locales. En un entorno limpio:

```bash
pip install open_corpus_co_es==0.1.1a4
python -m open_corpus_co_es --list
python -m open_corpus_co_es --download presidentes
```

Desde Python comprueba que `list_corpus()` devuelve 65 entradas, que `load_corpus("presidentes")`
devuelve 22 registros y que existe el registro de Abelardo de la Espriella con `fecha_inicio=2026`.
El estado de la publicación se verifica contra PyPI; construir el paquete localmente no lo publica.

La comprobación posterior de `0.1.1a4` confirmó los dos artefactos en PyPI y una
instalación limpia con el catálogo actualizado. Los resultados y las huellas están
en las [notas de versión]({{ '/versiones/' | relative_url }}).
