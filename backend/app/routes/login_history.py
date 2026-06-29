"""
Bharat Sahayak AI
Login History Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/login-history",
    tags=["Login History"],
)


@router.get("/")
def list_login_history():
    return {"message": "Login history endpoint ready"}


@router.get("/user/{user_id}")
def user_login_history(user_id: int):
    return {
        "message": "User login history endpoint ready",
        "user_id": user_id,
    }


@router.get("/failed")
def failed_logins():
    return {"message": "Failed login attempts endpoint ready"}


@router.get("/successful")
def successful_logins():
    return {"message": "Successful login attempts endpoint ready"}
