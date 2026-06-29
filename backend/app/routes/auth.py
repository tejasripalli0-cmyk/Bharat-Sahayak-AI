"""
Bharat Sahayak AI
Authentication Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
)
from app.utils.security import hash_password, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)

    existing_user = repository.get_by_email(request.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        phone_number=request.phone_number,
        password_hash=hash_password(request.password),
    )

    repository.create(user)

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "email": user.email,
    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)

    user = repository.get_by_email(request.email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        request.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
        "first_name": user.first_name,
    }


@router.post("/logout")
def logout():
    return {
        "message": "Logout endpoint ready",
    }


@router.post("/refresh")
def refresh_token():
    return {
        "message": "Refresh token endpoint ready",
    }


@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest):
    return {
        "message": "Forgot password request received",
        "email": request.email,
    }


@router.post("/reset-password")
def reset_password(request: ResetPasswordRequest):
    return {
        "message": "Reset password endpoint ready",
    }