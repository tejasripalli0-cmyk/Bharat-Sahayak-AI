"""
Bharat Sahayak AI
Feedback Repository
"""

from typing import Optional

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.models.feedback import Feedback


class FeedbackRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, feedback: Feedback) -> Feedback:
        self.db.add(feedback)
        self.db.commit()
        self.db.refresh(feedback)
        return feedback

    def get_by_id(self, feedback_id: int) -> Optional[Feedback]:
        return self.db.query(Feedback).filter(Feedback.id == feedback_id).first()

    def get_user_feedback(self, user_id: int, limit: int = 100) -> list[Feedback]:
        return (
            self.db.query(Feedback)
            .filter(Feedback.user_id == user_id)
            .order_by(desc(Feedback.created_at))
            .limit(limit)
            .all()
        )

    def average_rating(self) -> float:
        return (
            self.db.query(func.avg(Feedback.rating)).scalar()
            or 0.0
        )

    def unresolved(self) -> list[Feedback]:
        return (
            self.db.query(Feedback)
            .filter(Feedback.resolved.is_(False))
            .all()
        )

    def resolve(self, feedback: Feedback, notes: str | None = None) -> Feedback:
        feedback.resolved = True
        feedback.admin_notes = notes
        self.db.commit()
        self.db.refresh(feedback)
        return feedback

    def delete(self, feedback: Feedback) -> None:
        self.db.delete(feedback)
        self.db.commit()
