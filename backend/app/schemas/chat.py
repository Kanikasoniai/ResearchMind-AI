from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    page: int
    chunk_index: int


class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]