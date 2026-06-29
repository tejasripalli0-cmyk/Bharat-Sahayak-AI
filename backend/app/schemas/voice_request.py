"""
Bharat Sahayak AI
Voice Request Model
"""

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class VoiceRequest(BaseModel):
    __tablename__ = "voice_requests"

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    language: Mapped[str] = mapped_column(
        String(20),
        default="en",
        nullable=False,
    )

    audio_file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    transcription: Mapped[str | None] = mapped_column(String)

    processing_time_ms: Mapped[int | None] = mapped_column(Integer)

    provider: Mapped[str | None] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"<VoiceRequest(id={self.id}, language='{self.language}')>"
