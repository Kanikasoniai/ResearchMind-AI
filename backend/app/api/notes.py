from fastapi import APIRouter

from app.services.notes.notes_service import NotesService

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)

notes_service = NotesService()


@router.post("/")
async def generate_notes():
    return notes_service.generate_notes()