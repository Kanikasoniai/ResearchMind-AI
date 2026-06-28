import chromadb


class ChromaService:
    """
    Handles all interactions with ChromaDB.
    """

    def __init__(self):
        self.client = chromadb.PersistentClient(path="storage/chroma_db")

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
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def search(self, embedding, top_k=5):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )