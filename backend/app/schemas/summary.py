from enum import Enum

from pydantic import BaseModel


class SummaryType(str, Enum):
    BASIC = "basic"
    EXECUTIVE = "executive"
    STUDENT = "student"


class SummaryRequest(BaseModel):
    summary_type: SummaryType = SummaryType.BASIC


class SummaryResponse(BaseModel):
    success: bool
    summary: str
    chunks_used: int