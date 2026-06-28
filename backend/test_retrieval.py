from app.rag.retrieval_service import RetrievalService

retriever = RetrievalService()

result = retriever.retrieve(
    "What is artificial intelligence?"
)

print(result)