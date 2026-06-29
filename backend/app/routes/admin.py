"""
Bharat Sahayak AI
Admin Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def dashboard():
    return {"message": "Admin dashboard endpoint ready"}


@router.get("/users")
def users():
    return {"message": "Admin users endpoint ready"}


@router.get("/schemes")
def schemes():
    return {"message": "Admin schemes endpoint ready"}


@router.get("/analytics")
def analytics():
    return {"message": "Admin analytics endpoint ready"}
