"""
Bharat Sahayak AI
Authentication Service
"""

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def register(self, user: User) -> User:
        """
        Register a new user.
        Password hashing and validation should be
        handled before calling this method.
        """
        return self.user_repository.create(user)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repository.get_by_email(email)

    def get_user_by_phone(self, phone: str) -> User | None:
        return self.user_repository.get_by_phone(phone)

    def authenticate(self, email: str, password: str) -> User | None:
        """
        Placeholder for authentication logic.
        Replace with password hash verification.
        """
        user = self.user_repository.get_by_email(email)

        if user is None:
            return None

        # TODO:
        # Verify password hash here

        return user

    def update_profile(self, user: User) -> User:
        return self.user_repository.update(user)

    def delete_account(self, user: User) -> None:
        self.user_repository.delete(user)
