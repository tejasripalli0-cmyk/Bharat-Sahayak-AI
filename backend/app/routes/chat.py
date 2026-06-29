"""
Bharat Sahayak AI
Chat Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
def chat():
    return {
        "message": "Chat endpoint ready"
    }


@router.get("/history/{user_id}")
def chat_history(user_id: int):
    return {
        "message": "Chat history",
        "user_id": user_id,
    }


@router.delete("/history/{user_id}")
def clear_history(user_id: int):
    return {
        "message": "History cleared",
        "user_id": user_id,
    }