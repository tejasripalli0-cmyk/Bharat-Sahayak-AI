"""
Bharat Sahayak AI
Saved Scheme Model
"""

from sqlalchemy import Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class SavedScheme(BaseModel):
    __tablename__ = "saved_schemes"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "scheme_id",
            name="uq_saved_scheme_user_scheme",
        ),
    )

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

    is_favorite: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"<SavedScheme(user_id={self.user_id}, "
            f"scheme_id={self.scheme_id})>"
        )
