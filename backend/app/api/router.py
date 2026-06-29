from fastapi import APIRouter
from app.api.notes import router as notes_router
from app.api.health import router as health_router
from app.api.documents import router as documents_router
from app.api.chat import router as chat_router
from app.api.summary import router as summary_router

api_router = APIRouter()

api_router.include_router(notes_router)
api_router.include_router(health_router)
api_router.include_router(documents_router)
api_router.include_router(chat_router)
api_router.include_router(summary_router)