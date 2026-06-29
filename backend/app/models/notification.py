"""
Bharat Sahayak AI
Notification Model
"""

from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)

    notification_type: Mapped[str] = mapped_column(String(50), default="system")

    is_read: Mapped[bool] = mapped_column(Boolean, default=False)

    action_url: Mapped[str | None] = mapped_column(String(500))

    def __repr__(self) -> str:
        return f"<Notification(id={self.id}, user_id={self.user_id})>"
