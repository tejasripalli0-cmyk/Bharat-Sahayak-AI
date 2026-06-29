"""
Bharat Sahayak AI
Profile Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get("/")
def get_profile():
    return {"message": "Profile endpoint ready"}


@router.put("/")
def update_profile():
    return {"message": "Update profile endpoint ready"}


@router.get("/preferences")
def preferences():
    return {"message": "User preferences endpoint ready"}


@router.put("/preferences")
def update_preferences():
    return {"message": "Update preferences endpoint ready"}
