"""
Bharat Sahayak AI
User Preference Model
"""

from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class UserPreference(BaseModel):
    __tablename__ = "user_preferences"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        index=True,
        nullable=False,
    )

    preferred_language: Mapped[str] = mapped_column(
        String(20),
        default="en",
        nullable=False,
    )

    theme: Mapped[str] = mapped_column(
        String(20),
        default="light",
        nullable=False,
    )

    email_notifications: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    sms_notifications: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    voice_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"<UserPreference(user_id={self.user_id}, "
            f"language='{self.preferred_language}')>"
        )
