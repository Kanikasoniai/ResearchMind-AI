from pathlib import Path
import shutil

from fastapi import APIRouter, File, UploadFile

from app.services.pdf.validator import (
    validate_pdf,
    validate_file_size,
)
from app.services.pdf.extractor import extract_text
from app.services.pdf.metadata import extract_metadata

from app.services.text_processing.cleaner import clean_text
from app.services.text_processing.chunker import chunk_text

from app.utils.file_utils import generate_unique_filename

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

# Create uploads directory if it doesn't exist

UPLOAD_DIR = Path("storage/uploaded_papers")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a research paper PDF,
    validate it,
    save it,
    extract metadata,
    clean text,
    chunk text,
    and return document information.
    """

    # -----------------------------
    # Validate uploaded file
    # -----------------------------
    validate_pdf(file)
    validate_file_size(file)

    # -----------------------------
    # Generate unique filename
    # -----------------------------
    unique_filename = generate_unique_filename(file.filename)

    # -----------------------------
    # Save uploaded file
    # -----------------------------
    file_path = UPLOAD_DIR / unique_filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # -----------------------------
    # Extract metadata
    # -----------------------------
    metadata = extract_metadata(str(file_path))

    # -----------------------------
    # Extract text
    # -----------------------------
    extracted_text = extract_text(str(file_path))

    # -----------------------------
    # Clean extracted text
    # -----------------------------
    cleaned_text = clean_text(extracted_text)

    # -----------------------------
    # Split text into chunks
    # -----------------------------
    chunks = chunk_text(cleaned_text)

    # -----------------------------
    # Return response
    # -----------------------------
    return {
        "success": True,
        "message": "PDF uploaded successfully.",
        "document": {
            "original_filename": file.filename,
            "stored_filename": unique_filename,
            "pages": metadata["pages"],
            "title": metadata["title"],
            "author": metadata["author"],
            "characters": len(cleaned_text),
            "chunks": len(chunks),
        },
    }
    