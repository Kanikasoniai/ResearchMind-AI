class ContextRanker:
    """
    Cleans retrieved chunks before sending them to the LLM.
    """

    @staticmethod
    def rank(results, max_chunks: int = 5):

        documents = results["documents"]
        metadatas = results["metadatas"]

        ranked_documents = []
        ranked_metadata = []

        seen = set()

        for document, metadata in zip(documents, metadatas):

            if document in seen:
                continue

            seen.add(document)

            ranked_documents.append(document)
            ranked_metadata.append(metadata)

            if len(ranked_documents) >= max_chunks:
                break

        return {
            "documents": ranked_documents,
            "metadatas": ranked_metadata,
        }