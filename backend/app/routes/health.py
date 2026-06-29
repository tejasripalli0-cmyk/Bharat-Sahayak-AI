"""
Bharat Sahayak AI
Health Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "Bharat Sahayak AI",
    }


@router.get("/ping")
def ping():
    return {"message": "pong"}
