from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    pages: int
    title: str | None
    author: str | None
    message: str