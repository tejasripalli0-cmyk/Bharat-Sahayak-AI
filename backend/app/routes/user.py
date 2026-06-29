"""
Bharat Sahayak AI
User Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.user_repository import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    users = repository.list_users()

    return [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "state": user.state,
            "district": user.district,
            "occupation": user.occupation,
            "preferred_language": user.preferred_language,
            "is_active": user.is_active,
            "is_verified": user.is_verified,
        }
        for user in users
    ]


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    repository = UserRepository(db)

    user = repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "state": user.state,
        "district": user.district,
        "occupation": user.occupation,
        "preferred_language": user.preferred_language,
        "is_active": user.is_active,
        "is_verified": user.is_verified,
    }


@router.put("/{user_id}")
def update_user(user_id: int):
    return {
        "message": "Update user endpoint will be implemented next.",
        "user_id": user_id,
    }


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "Delete user endpoint will be implemented next.",
        "user_id": user_id,
    }


@router.get("/{user_id}/profile")
def get_profile(user_id: int):
    return {
        "message": "Profile endpoint will be implemented next.",
        "user_id": user_id,
    }


@router.put("/{user_id}/profile")
def update_profile(user_id: int):
    return {
        "message": "Update profile endpoint will be implemented next.",
        "user_id": user_id,
    }