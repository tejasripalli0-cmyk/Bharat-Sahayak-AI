"""
Bharat Sahayak AI
Application History Model
"""

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class ApplicationHistory(BaseModel):
    __tablename__ = "application_history"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
        nullable=False,
    )

    scheme_id: Mapped[int] = mapped_column(
        ForeignKey("government_schemes.id"),
        index=True,
        nullable=False,
    )

    application_status: Mapped[str] = mapped_column(
        String(50),
        default="Draft",
        nullable=False,
    )

    application_reference: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
    )

    remarks: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return (
            f"<ApplicationHistory(user_id={self.user_id}, "
            f"scheme_id={self.scheme_id}, "
            f"status='{self.application_status}')>"
        )
