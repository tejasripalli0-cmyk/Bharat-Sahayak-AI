"""
Bharat Sahayak AI
Scheme Model
"""

from sqlalchemy import Boolean, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class Scheme(BaseModel):
    __tablename__ = "schemes"

    # ---------------------------------------------------------
    # Basic Information
    # ---------------------------------------------------------

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    ministry: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    state: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        default="All India",
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Eligibility Rules
    # ---------------------------------------------------------

    minimum_age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    maximum_age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    gender: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    occupation: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    education_level: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    category_allowed: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    income_limit: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    eligibility: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Benefits
    # ---------------------------------------------------------

    benefits: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    benefit_amount: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    # ---------------------------------------------------------
    # Documents
    # ---------------------------------------------------------

    required_documents: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    official_website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    application_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    application_deadline: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    def __repr__(self):
        return f"<Scheme(id={self.id}, name='{self.name}')>"