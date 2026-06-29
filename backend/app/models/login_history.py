"""
Bharat Sahayak AI
Login History Model
"""

from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class LoginHistory(BaseModel):
    __tablename__ = "login_history"

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    login_method: Mapped[str] = mapped_column(
        String(50),
        default="email",
        nullable=False,
    )

    ip_address: Mapped[str | None] = mapped_column(String(50))
    device: Mapped[str | None] = mapped_column(String(255))
    user_agent: Mapped[str | None] = mapped_column(String)
    success: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"<LoginHistory(id={self.id}, success={self.success})>"
