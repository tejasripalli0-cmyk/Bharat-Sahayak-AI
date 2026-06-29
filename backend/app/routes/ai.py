"""
Bharat Sahayak AI
AI Router
"""

from pydantic import BaseModel
from fastapi import APIRouter

from app.services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)

ai_service = AIService()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def ai_chat(request: ChatRequest):
    return ai_service.generate_response(
        prompt=request.message
    )


@router.post("/summarize")
def summarize(request: ChatRequest):
    return {
        "summary": ai_service.summarize(
            request.message
        )
    }


@router.post("/classify")
def classify(request: ChatRequest):
    return ai_service.classify_intent(
        request.message
    )


@router.post("/entities")
def extract_entities(request: ChatRequest):
    return ai_service.extract_entities(
        request.message
    )