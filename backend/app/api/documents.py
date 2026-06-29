from fastapi import APIRouter, File, UploadFile

from app.services.document.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

document_service = DocumentService()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return await document_service.process_document(file)