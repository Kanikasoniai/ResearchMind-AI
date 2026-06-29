from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat.chat_service import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

chat_service = ChatService()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):
    """
    Ask a question about the uploaded research papers.
    """
    return chat_service.ask(request.question)