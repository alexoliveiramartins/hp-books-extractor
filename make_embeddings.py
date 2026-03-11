# usa a lib sentence-transformers (pip install sentence-transformers)

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("BAAI/bge-base-en-v1.5")

def make_embedding(text: str):
    embedding = model.encode(text)
    return embedding

