import json
import os
import sys
import json

markdown_path = './output/output.md'

if not (os.path.isfile(markdown_path)):
    print("Txt file does not exist")
    sys.exit()

with open(markdown_path, 'r') as md_file:
    raw_book = md_file.read()
    book_chunks = raw_book.split('\n')

with open("./output/chunks.jsonl", "w") as file:
    current_chapter = 0
    current_book = -1           # -1 por que tem um "CONTENTS" pro conteudo da colecao
    for chunk in book_chunks:
        if(chunk == '' or chunk.lower().startswith('**==> picture')):
            continue
        if(chunk.startswith("## CONTENTS")):
            # print(f'Book {current_book} chapters: {current_chapter}')
            current_book += 1
            current_chapter = 0
        if(
            chunk.startswith('**CHAPTER')
         or chunk.startswith("## **CHAPTER")
         or chunk.startswith('CHAPTER')
         ):
            current_chapter += 1
        chunk_json = (
            {
                "book": current_book,
                "chapter": current_chapter,
                "text": chunk
            }
        )
        file.write(json.dumps(chunk_json, ensure_ascii=False) + "\n")
        # print(chunk)

print(f'Number of chunks: {len(book_chunks)}')