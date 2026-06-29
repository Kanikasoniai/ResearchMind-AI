import chromadb


class ChromaService:
    """
    Handles all interactions with ChromaDB.
    """

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="storage/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="research_papers"
        )

    def add_chunks(
        self,
        ids,
        embeddings,
        documents,
        metadatas,
    ):
        """
        Store document chunks and their embeddings.
        """

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def search(
        self,
        embedding,
        top_k: int = 5,
    ):
        """
        Search for the most relevant document chunks.
        """

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        return {
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "distances": results["distances"][0],
        }

    def delete_document(
        self,
        document_id: str,
    ):
        """
        Delete all chunks belonging to a document.
        """

        self.collection.delete(
            where={
                "document_id": document_id
            }
        )

    def count_documents(self):
        """
        Return the total number of stored chunks.
        """

        return self.collection.count()