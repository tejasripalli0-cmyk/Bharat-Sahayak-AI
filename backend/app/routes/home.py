"""
Bharat Sahayak AI
Home Router
"""

from fastapi import APIRouter

router = APIRouter(
    tags=["Home"],
)


@router.get("/")
def home():
    return {
        "project": "Bharat Sahayak AI",
        "status": "running",
        "message": "Welcome to Bharat Sahayak AI API"
    }


@router.get("/about")
def about():
    return {
        "name": "Bharat Sahayak AI",
        "description": "AI-powered multilingual government scheme assistant"
    }


@router.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
