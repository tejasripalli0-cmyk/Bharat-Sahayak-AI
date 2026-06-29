"""
Bharat Sahayak AI
Export Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/users")
def export_users():
    return {"message": "User export endpoint ready"}


@router.get("/schemes")
def export_schemes():
    return {"message": "Scheme export endpoint ready"}


@router.get("/applications")
def export_applications():
    return {"message": "Application export endpoint ready"}
