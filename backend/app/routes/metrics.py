"""
Bharat Sahayak AI
Metrics Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.get("/overview")
def overview():
    return {"message": "Metrics overview endpoint ready"}


@router.get("/users")
def users():
    return {"message": "User metrics endpoint ready"}


@router.get("/schemes")
def schemes():
    return {"message": "Scheme metrics endpoint ready"}


@router.get("/ai")
def ai():
    return {"message": "AI metrics endpoint ready"}
