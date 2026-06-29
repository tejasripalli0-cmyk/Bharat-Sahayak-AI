"""
Bharat Sahayak AI
Dashboard Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/overview")
def overview():
    return {"message": "Dashboard overview endpoint ready"}


@router.get("/stats")
def stats():
    return {"message": "Dashboard statistics endpoint ready"}


@router.get("/recent")
def recent_activity():
    return {"message": "Recent activity endpoint ready"}


@router.get("/summary")
def summary():
    return {"message": "Dashboard summary endpoint ready"}
