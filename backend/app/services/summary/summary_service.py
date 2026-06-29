from app.prompts.summary_prompts import SUMMARY_PROMPTS
from app.schemas.summary import SummaryType
from app.services.ai_engine.ai_engine import AIEngine


class SummaryService:
    """
    Handles AI-generated summaries of research papers.
    """

    def __init__(self):
        self.engine = AIEngine()

    def summarize(self, summary_type: SummaryType):

        prompt = SUMMARY_PROMPTS[summary_type.value]

        result = self.engine.generate(
            instruction=prompt,
            question="Summarize the uploaded research paper.",
            top_k=10,
        )

        return {
            "success": True,
            "summary_type": summary_type.value,
            "summary": result["answer"],
            "sources": result["sources"],
            "chunks_used": result["retrieved_chunks"],
            "model": "gemini-2.5-flash",
        }