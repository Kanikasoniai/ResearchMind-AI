from app.rag.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

vector = embedding_service.generate_embedding(
    "Transformers are used in natural language processing."
)

print(f"Vector length: {len(vector)}")
print(vector[:10])