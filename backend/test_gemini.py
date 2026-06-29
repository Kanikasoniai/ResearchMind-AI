print("Step 1: Starting test...")

from app.services.llm.gemini_service import GeminiService

print("Step 2: Service imported")

service = GeminiService()

print("Step 3: Service initialized")

answer = service.generate_answer(
    "Explain Retrieval Augmented Generation in one paragraph."
)

print("Step 4: Gemini responded")

print(answer)

print("Step 5: Finished")