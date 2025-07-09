from setuptools import setup, find_packages

setup(
    name="open_corpus_co_es",
    version="0.1.1a2",
    description="Corpus en español de Colombia para PLN",
    author="Luis Gabriel Moreno Sandoval",
    author_email="morenoluis@javeriana.edu.co",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "nltk", "pandas", "gdown", "pyarrow", "fastparquet", "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_data={
        "open_corpus_co_es": ["catalog.json"]
    },
)
