"""
Bharat Sahayak AI
Translation Model
"""

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class Translation(BaseModel):
    __tablename__ = "translations"

    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), index=True)

    source_language: Mapped[str] = mapped_column(String(20), nullable=False)
    target_language: Mapped[str] = mapped_column(String(20), nullable=False)

    source_text: Mapped[str] = mapped_column(Text, nullable=False)
    translated_text: Mapped[str] = mapped_column(Text, nullable=False)

    translation_provider: Mapped[str | None] = mapped_column(String(100))

    def __repr__(self) -> str:
        return (
            f"<Translation(id={self.id}, "
            f"{self.source_language}->{self.target_language})>"
        )
