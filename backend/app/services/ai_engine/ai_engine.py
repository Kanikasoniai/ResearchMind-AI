from app.rag.context_ranker import ContextRanker
from app.rag.prompt_builder import PromptBuilder
from app.rag.retrieval_service import RetrievalService
from app.services.llm.gemini_service import GeminiService


class AIEngine:
    """
    Central AI Engine responsible for Retrieval-Augmented Generation.
    Every AI feature in ResearchMind AI uses this engine.
    """

    def __init__(self):
        self.retriever = RetrievalService()
        self.gemini = GeminiService()

    def generate(
        self,
        instruction: str,
        question: str,
        top_k: int = 5,
    ):

        retrieval = self.retriever.retrieve(
            question,
            top_k=top_k,
        )

        ranked = ContextRanker.rank(retrieval)

        context = "\n\n".join(
            ranked["documents"]
        )

        prompt = f"""
{instruction}

{PromptBuilder.build_prompt(
    question=question,
    context=context,
)}
"""

        answer = self.gemini.generate_answer(prompt)

        return {
            "answer": answer,
            "sources": ranked["metadatas"],
            "retrieved_chunks": len(ranked["documents"]),
        }