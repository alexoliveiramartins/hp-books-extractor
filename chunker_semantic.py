import json
import os
import sys
import numpy as np
from make_embeddings import make_embedding

markdown_path = './output/output_epub.md'

if not os.path.isfile(markdown_path):
    print(f"{markdown_path}: File does not exist")
    sys.exit()

with open(markdown_path, 'r') as md_file:
    raw_book = md_file.read()

book_paragraphs = raw_book.split('\n')

SIM_THRESHOLD = 0.75
MIN_CHARS = 120

def cosine_sim(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


with open("./output/chunks_with_embeddings.jsonl", "w") as file:

    current_chapter = 0
    current_book = -1

    prev_embedding = None
    current_text = ""
    current_embedding = None

    for i in range(len(book_paragraphs)):

        paragraph = book_paragraphs[i].strip()

        if paragraph == '' or paragraph.lower().startswith('**==> picture'):
            continue

        if paragraph.startswith("## CONTENTS"):
            current_book += 1
            current_chapter = 0

        if (
            paragraph.startswith('**CHAPTER')
            or paragraph.startswith("## **CHAPTER")
            or paragraph.startswith('CHAPTER')
        ):
            current_chapter += 1

        emb = make_embedding(paragraph)

        if hasattr(emb, 'tolist'):
            emb = emb.tolist()

        if prev_embedding is None:
            current_text = paragraph
            current_embedding = emb
            prev_embedding = emb
            continue

        sim = cosine_sim(prev_embedding, emb)

        should_merge = (
            len(current_text) < MIN_CHARS
            or paragraph.startswith("“")
            or paragraph.startswith("—")
            or sim > SIM_THRESHOLD
        )

        if should_merge:
            current_text += " " + paragraph
            prev_embedding = emb
        else:
            full_chunk_embedding = make_embedding(current_text)
            if hasattr(full_chunk_embedding, 'tolist'):
                full_chunk_embedding = full_chunk_embedding.tolist()

            chunk_json = {
                "book": current_book,
                "chapter": current_chapter,
                "text": current_text,
                "embedding": full_chunk_embedding
            }

            file.write(json.dumps(chunk_json, ensure_ascii=False) + "\n")

            current_text = paragraph
            current_embedding = emb
            prev_embedding = emb

    if current_text:
        full_chunk_embedding = make_embedding(current_text)
        if hasattr(full_chunk_embedding, 'tolist'):
            full_chunk_embedding = full_chunk_embedding.tolist()

        chunk_json = {
            "book": current_book,
            "chapter": current_chapter,
            "text": current_text,
            "embedding": full_chunk_embedding
        }

        file.write(json.dumps(chunk_json, ensure_ascii=False) + "\n")

print("Semantic chunking with embeddings complete.")