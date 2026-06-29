from app.rag.embedding_service import EmbeddingService
from app.vectorstore.chroma_service import ChromaService


class RetrievalService:
    """
    Retrieves the most relevant chunks from ChromaDB.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()

    def retrieve(self, question: str, top_k: int = 5):

        query_embedding = self.embedding_service.generate_embedding(question)

        results = self.chroma_service.search(
            embedding=query_embedding,
            top_k=top_k,
        )

        return results