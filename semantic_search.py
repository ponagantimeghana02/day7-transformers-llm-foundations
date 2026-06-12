from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "Python is used for AI development",
    "Machine learning helps computers learn patterns",
    "Transformers power modern LLMs",
    "Cloud computing provides scalable infrastructure",
    "Databases store application data"
]
model = SentenceTransformer('all-MiniLM-L6-v2')

document_embeddings = model.encode(documents)

print("Document Embeddings Generated Successfully!")
print("Embedding Dimension:", document_embeddings.shape[1])

query = input("\nEnter your search query: ")
query_embedding = model.encode([query])

similarity_scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

top_indices = np.argsort(similarity_scores)[::-1][:3]

print("\nTop 3 Relevant Documents:")
for rank, idx in enumerate(top_indices, start=1):
    print(f"\n{rank}. {documents[idx]}")
    print(f"   Similarity Score: {similarity_scores[idx]:.4f}")