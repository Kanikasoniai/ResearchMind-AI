from app.prompts.notes_prompts import NOTES_PROMPT
from app.services.ai_engine.ai_engine import AIEngine


class NotesService:

    def __init__(self):
        self.engine = AIEngine()

    def generate_notes(self):

        result = self.engine.generate(
            instruction=NOTES_PROMPT,
            question="Generate detailed study notes for this research paper.",
            top_k=10,
        )

        return {
            "success": True,
            "notes": result["answer"],
            "chunks_used": result["retrieved_chunks"],
        }