from pathlib import Path
import shutil
from uuid import uuid4

from fastapi import UploadFile, HTTPException

from app.services.pdf.validator import (
    validate_pdf,
    validate_file_size,
)

from app.services.pdf.extractor import extract_text
from app.services.pdf.metadata import extract_metadata

from app.services.text_processing.cleaner import clean_text
from app.services.text_processing.chunker import chunk_text

from app.rag.embedding_service import EmbeddingService
from app.vectorstore.chroma_service import ChromaService


class DocumentService:
    """
    Coordinates the complete document ingestion pipeline.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()

        self.upload_dir = Path("storage/uploaded_papers")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def process_document(self, file: UploadFile):

        # -------------------------
        # Validation
        # -------------------------
        validate_pdf(file)
        validate_file_size(file)

        # -------------------------
        # Save file
        # -------------------------
        document_id = str(uuid4())

        extension = Path(file.filename).suffix
        stored_filename = f"{document_id}{extension}"

        file_path = self.upload_dir / stored_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -------------------------
        # Extract
        # -------------------------
        metadata = extract_metadata(str(file_path))

        extracted_text = extract_text(str(file_path))

        cleaned_text = clean_text(extracted_text)

        chunks = chunk_text(cleaned_text)

        # -------------------------
        # DEBUG
        # -------------------------
        print("\n" + "=" * 60)
        print("DEBUG DOCUMENT PIPELINE")
        print("=" * 60)
        print("Extracted text length:", len(cleaned_text))
        print("Number of chunks:", len(chunks))

        if len(chunks) > 0:
            print("First chunk preview:")
            print(chunks[0][:300])
        else:
            print("No chunks generated!")

        print("=" * 60)

        # -------------------------
        # Generate embeddings
        # -------------------------
        embeddings = self.embedding_service.generate_embeddings(chunks)

        print("Embeddings generated:", len(embeddings))
        print("=" * 60)

        if len(embeddings) == 0:
            raise HTTPException(
                status_code=500,
                detail="No embeddings were generated."
            )

        ids = []
        metadatas = []

        for index in range(len(chunks)):
            ids.append(f"{document_id}_{index}")

            metadatas.append(
                {
                    "document_id": document_id,
                    "page": 1,
                    "chunk_index": index,
                }
            )

        # -------------------------
        # Store vectors
        # -------------------------
        self.chroma_service.add_chunks(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )

        # -------------------------
        # Response
        # -------------------------
        return {
            "success": True,
            "message": "Document indexed successfully.",
            "document": {
                "document_id": document_id,
                "original_filename": file.filename,
                "stored_filename": stored_filename,
                "pages": metadata["pages"],
                "title": metadata["title"],
                "author": metadata["author"],
                "characters": len(cleaned_text),
                "chunks": len(chunks),
            },
        }