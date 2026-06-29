from pydantic import BaseModel


class NotesRequest(BaseModel):
    style: str = "student"


class NotesResponse(BaseModel):
    success: bool
    notes: str
    chunks_used: int