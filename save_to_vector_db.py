# pip install chromadb
import chromadb
import json
from make_embeddings import make_embedding

client = chromadb.PersistentClient(path="./output/vector_db")

collection = client.get_or_create_collection(name="hp_books")

with open("./output/chunks.jsonl") as f:
    for i, line in enumerate(f):
        print(f"Chunk atual: {i}")
        chunk = json.loads(line)

        collection.add(
            documents=[chunk["text"]],
            ids=[str(i)],
            embeddings=[make_embedding(chunk['text'])],
            metadatas=[{
                "book": chunk["book"],
                "chapter": chunk["chapter"]
            }]
        )