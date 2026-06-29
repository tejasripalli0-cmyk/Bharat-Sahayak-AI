"""
Bharat Sahayak AI
Report Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/user/{user_id}")
def user_report(user_id: int):
    return {
        "message": "User report endpoint ready",
        "user_id": user_id,
    }


@router.get("/scheme/{scheme_id}")
def scheme_report(scheme_id: int):
    return {
        "message": "Scheme report endpoint ready",
        "scheme_id": scheme_id,
    }


@router.get("/system")
def system_report():
    return {
        "message": "System report endpoint ready"
    }
