from fastapi import APIRouter

from app.schemas.summary import SummaryRequest
from app.services.summary.summary_service import SummaryService

router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)

summary_service = SummaryService()


@router.post("/")
async def summarize(request: SummaryRequest):

    return summary_service.summarize(
        request.summary_type
    )