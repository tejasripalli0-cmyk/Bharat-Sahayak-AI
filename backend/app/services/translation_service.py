"""
Bharat Sahayak AI
Translation Service
"""

from sqlalchemy.orm import Session

from app.models.translation import Translation
from app.repositories.translation_repository import TranslationRepository


class TranslationService:
    def __init__(self, db: Session):
        self.db = db
        self.translation_repository = TranslationRepository(db)

    def create_translation(self, translation: Translation) -> Translation:
        return self.translation_repository.create(translation)

    def get_history(self, user_id: int):
        return self.translation_repository.get_user_history(user_id)

    def translate(
        self,
        source_language: str,
        target_language: str,
        source_text: str,
    ) -> dict:
        """
        Placeholder for translation provider integration.
        """
        return {
            "source_language": source_language,
            "target_language": target_language,
            "translated_text": source_text,
        }
