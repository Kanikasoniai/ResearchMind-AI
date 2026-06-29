from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import generic_exception_handler

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the AI Research Paper Assistant",
    version=settings.app_version,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name} 🚀",
        "status": "Backend is running successfully",
        "version": settings.app_version,
    }


@app.get("/test-error")
def test_error():
    raise Exception("This is a test exception.")
