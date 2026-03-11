import chromadb
from make_embeddings import make_embedding

client = chromadb.PersistentClient(path="./output/vector_db")

collection = client.get_collection("hp_books")

results = collection.query(
    query_embeddings=[make_embedding("query: Physical description of Dumbledore")],
    n_results=3
)

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print(f'Book {meta["book"]}, Chapter {meta["chapter"]}')
    print(doc)
    print()