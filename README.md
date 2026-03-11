# hp-books-extractor

Esse script tem como objetivo extrair informações dos livros de Harry Potter.
Foi utilizado pela praticidade a versão completa (The Complete Edition).

Dependencias: pypdf,

## Script 1 - extract_text.py

- Extrai o texto do pdf usando pypdf

```bash
$ python3 extract_text.py
```

O arquivo de saída será um txt `book.txt` na pasta ./data/

## Script 2 - parse_markdown.py

- Converte o arquivo pdf para markdown usando a lib pymupdf4llm

```bash
$ python3 parse_markdown.py
```

## Script 3 - chunker.py

- Cria jsons de chunks feitas a partir do arquivo .md

```bash
$ python3 chunker.py
```

## Scrpit 4 - save_to_vector_db.py (+make_embeddings)

- Salva cada chunk com o seu embedding em um BD Vetorial local (chromadb)

```bash
$ python3 save_to_vector_db.py
```

## Script 5 - test_vectord_db.py

- Testa o BD vetorial com queries (embbeded)

```bash
$ python3 test_vector_db.py
```
