from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
docs = ["Reset password", "Login issues", "Subscription help"]
vectors = model.encode(docs)

index = faiss.IndexFlatL2(len(vectors[0]))
index.add(np.array(vectors))

def retrieve_context(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=1)
    return docs[I[0][0]]
