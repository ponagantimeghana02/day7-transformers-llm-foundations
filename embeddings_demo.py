from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sentences
sentences = [
    "AI is changing the world.",
    "Artificial Intelligence is transforming industries.",
    "I love playing cricket."
]

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(sentences)

# Display embedding dimensions
print("Embedding Dimensions:")
for i, embedding in enumerate(embeddings, start=1):
    print(f"Sentence {i}: {embedding.shape}")

# Calculate cosine similarity
similarity_matrix = cosine_similarity(embeddings)

print("\nCosine Similarity Matrix:")
print(similarity_matrix)

# Display pairwise similarities
print("\nPairwise Similarities:")
print(f"Sentence 1 ↔ Sentence 2: {similarity_matrix[0][1]:.4f}")
print(f"Sentence 1 ↔ Sentence 3: {similarity_matrix[0][2]:.4f}")
print(f"Sentence 2 ↔ Sentence 3: {similarity_matrix[1][2]:.4f}")

# Explanation
print("\nExplanation:")
print("Sentence 1 and Sentence 2 are semantically similar because both discuss AI/Artificial Intelligence and its impact.")
print("Sentence 3 talks about cricket, which is a completely different topic.")
print("Therefore, the cosine similarity between Sentence 1 and Sentence 2 is much higher than their similarity with Sentence 3.")