from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python is a popular programming language.",
    "Machine learning enables systems to learn from data.",
    "Deep learning uses neural networks.",
    "Transformers power modern large language models.",
    "Artificial Intelligence is changing industries.",
    "Cloud computing provides scalable infrastructure.",
    "Databases store and manage application data.",
    "Cybersecurity protects systems from threats.",
    "Natural Language Processing helps computers understand text.",
    "Computer Vision enables image recognition.",
    "Data Science extracts insights from data.",
    "Pandas is used for data manipulation.",
    "NumPy supports numerical computations.",
    "Matplotlib helps visualize data.",
    "Scikit-learn provides machine learning algorithms.",
    "TensorFlow is a deep learning framework.",
    "PyTorch is popular for AI research.",
    "Chatbots use NLP techniques.",
    "Recommendation systems improve user experience.",
    "Semantic search understands meaning.",
    "Embeddings represent text as vectors.",
    "Vector databases store embeddings.",
    "RAG combines retrieval and generation.",
    "LLMs generate human-like text.",
    "Attention mechanisms capture context.",
    "Tokenization splits text into tokens.",
    "BERT is a transformer-based model.",
    "GPT models are autoregressive.",
    "Fine-tuning adapts models to tasks.",
    "Prompt engineering improves responses.",
    "APIs allow software communication.",
    "REST APIs are widely used.",
    "Frontend development uses HTML CSS and JavaScript.",
    "React is a frontend library.",
    "Node.js runs JavaScript on servers.",
    "Express simplifies backend development.",
    "MongoDB is a NoSQL database.",
    "SQL databases store structured data.",
    "Git tracks code changes.",
    "GitHub hosts software repositories.",
    "Docker enables containerization.",
    "Kubernetes manages containers.",
    "Linux powers many servers.",
    "Operating systems manage hardware resources.",
    "Algorithms solve computational problems.",
    "Data structures organize information efficiently.",
    "Trees and graphs are common data structures.",
    "Sorting algorithms arrange data.",
    "Binary search is efficient for sorted lists.",
    "Software testing ensures quality."
]


print("Generating embeddings...")

document_embeddings = model.encode(documents)

print(f"Stored {len(documents)} documents.")
print(f"Embedding Dimension: {document_embeddings.shape[1]}")


query = input("\nEnter your search query: ")

query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

top_k = 5

top_indices = np.argsort(similarities)[::-1][:top_k]

print("\n" + "=" * 60)
print("TOP MATCHING DOCUMENTS")
print("=" * 60)

for rank, idx in enumerate(top_indices, start=1):
    print(f"\nRank #{rank}")
    print(f"Document : {documents[idx]}")
    print(f"Similarity Score : {similarities[idx]:.4f}")