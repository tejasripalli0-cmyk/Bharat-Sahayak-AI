"""
Bharat Sahayak AI
Notification Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


@router.get("/")
def list_notifications():
    return {"message": "List notifications endpoint ready"}


@router.get("/unread/{user_id}")
def unread_notifications(user_id: int):
    return {
        "message": "Unread notifications endpoint ready",
        "user_id": user_id,
    }


@router.put("/read/{notification_id}")
def mark_read(notification_id: int):
    return {
        "message": "Notification marked as read",
        "notification_id": notification_id,
    }
