from fastapi import FastAPI
from app.core.logger import logger
from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the AI Research Paper Assistant",
    version=settings.app_version,
)

app.include_router(api_router, prefix=settings.api_prefix)
from app.core.exceptions import generic_exception_handler

app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/test-error")
def test_error():
    raise Exception("This is a test exception.")

    return {
        "message": f"Welcome to {settings.app_name} 🚀",
        "status": "Backend is running successfully",
        "version": settings.app_version,
    }

