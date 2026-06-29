"""
Bharat Sahayak AI
Login History Repository
"""

from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.login_history import LoginHistory


class LoginHistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, history: LoginHistory) -> LoginHistory:
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history

    def get_by_id(self, history_id: int) -> Optional[LoginHistory]:
        return self.db.query(LoginHistory).filter(LoginHistory.id == history_id).first()

    def get_user_history(self, user_id: int):
        return (
            self.db.query(LoginHistory)
            .filter(LoginHistory.user_id == user_id)
            .order_by(desc(LoginHistory.created_at))
            .all()
        )

    def successful_logins(self, user_id: int):
        return (
            self.db.query(LoginHistory)
            .filter(LoginHistory.user_id == user_id)
            .filter(LoginHistory.success.is_(True))
            .all()
        )

    def failed_logins(self, user_id: int):
        return (
            self.db.query(LoginHistory)
            .filter(LoginHistory.user_id == user_id)
            .filter(LoginHistory.success.is_(False))
            .all()
        )
