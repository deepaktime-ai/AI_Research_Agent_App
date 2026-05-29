from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory DB
documents = []
vectors = None
index = None


def add_documents(text_chunks):
    global documents, vectors, index

    embeddings = model.encode(text_chunks)

    if index is None:
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        vectors = np.array(embeddings)
        index.add(vectors)
    else:
        index.add(np.array(embeddings))
        vectors = np.vstack([vectors, embeddings])

    documents.extend(text_chunks)


def search(query, k=3):
    global index, documents

    if index is None:
        return []

    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), k)

    results = [documents[i] for i in indices[0] if i < len(documents)]
    return results