"""
Bharat Sahayak AI
Application Repository
"""

from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.application_history import ApplicationHistory


class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, application: ApplicationHistory) -> ApplicationHistory:
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application

    def get_by_id(self, application_id: int) -> Optional[ApplicationHistory]:
        return (
            self.db.query(ApplicationHistory)
            .filter(ApplicationHistory.id == application_id)
            .first()
        )

    def get_user_applications(self, user_id: int):
        return (
            self.db.query(ApplicationHistory)
            .filter(ApplicationHistory.user_id == user_id)
            .order_by(desc(ApplicationHistory.created_at))
            .all()
        )

    def get_scheme_applications(self, scheme_id: int):
        return (
            self.db.query(ApplicationHistory)
            .filter(ApplicationHistory.scheme_id == scheme_id)
            .all()
        )

    def update_status(
        self,
        application: ApplicationHistory,
        status: str,
    ) -> ApplicationHistory:
        application.application_status = status
        self.db.commit()
        self.db.refresh(application)
        return application

    def delete(self, application: ApplicationHistory) -> None:
        self.db.delete(application)
        self.db.commit()
