from app.vectorstore.chroma_service import ChromaService

db = ChromaService()

db.add_chunks(
    ids=["chunk1"],
    embeddings=[[0.1] * 384],
    documents=["This is a test chunk."],
    metadatas=[
        {
            "document_id": "doc1",
            "page": 1,
            "chunk_index": 0,
        }
    ],
)

print("Stored successfully!")

result = db.search(
    embedding=[0.1] * 384
)

print(result)