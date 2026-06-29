"""
Bharat Sahayak AI
AI Service
"""

from groq import Groq

from app.core.config import get_settings


class AIService:
    def __init__(self):
        settings = get_settings()
        self.client = Groq(api_key=settings.GROQ_API_KEY)

    def generate_response(
        self,
        prompt: str,
        context: str | None = None,
        language: str = "en",
    ) -> dict:

        final_prompt = prompt

        if context:
            final_prompt = f"""
Context:
{context}

User Question:
{prompt}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Bharat Sahayak AI, an AI assistant that helps "
                        "Indian citizens understand government schemes. "
                        "Reply clearly, accurately and politely."
                    ),
                },
                {
                    "role": "user",
                    "content": final_prompt,
                },
            ],
            temperature=0.3,
            max_tokens=1024,
        )

        return {
            "response": response.choices[0].message.content,
            "language": language,
            "context_used": context is not None,
            "provider": "Groq",
            "model": "llama-3.3-70b-versatile",
        }

    def summarize(self, text: str) -> str:
        return self.generate_response(
            f"Summarize the following:\n\n{text}"
        )["response"]

    def classify_intent(self, text: str) -> dict:
        return self.generate_response(
            f"Classify the intent of this query:\n\n{text}"
        )

    def extract_entities(self, text: str):
        return self.generate_response(
            f"Extract important entities from:\n\n{text}"
        )