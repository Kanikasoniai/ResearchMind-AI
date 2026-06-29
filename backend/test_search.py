from app.rag.embedding_service import EmbeddingService
from app.vectorstore.chroma_service import ChromaService

embedding = EmbeddingService()
db = ChromaService()

question = "What is this document about?"

query = embedding.generate_embedding(question)

results = db.search(query)

print(results)