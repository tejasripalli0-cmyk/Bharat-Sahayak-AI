"""
Bharat Sahayak AI
Translation Repository
"""

from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.translation import Translation


class TranslationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, translation: Translation) -> Translation:
        self.db.add(translation)
        self.db.commit()
        self.db.refresh(translation)
        return translation

    def get_by_id(self, translation_id: int) -> Optional[Translation]:
        return (
            self.db.query(Translation)
            .filter(Translation.id == translation_id)
            .first()
        )

    def get_user_history(
        self,
        user_id: int,
        limit: int = 100,
    ) -> list[Translation]:
        return (
            self.db.query(Translation)
            .filter(Translation.user_id == user_id)
            .order_by(desc(Translation.created_at))
            .limit(limit)
            .all()
        )

    def find_by_languages(
        self,
        source: str,
        target: str,
    ) -> list[Translation]:
        return (
            self.db.query(Translation)
            .filter(Translation.source_language == source)
            .filter(Translation.target_language == target)
            .all()
        )

    def update(self, translation: Translation) -> Translation:
        self.db.commit()
        self.db.refresh(translation)
        return translation

    def delete(self, translation: Translation) -> None:
        self.db.delete(translation)
        self.db.commit()
