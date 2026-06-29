"""
Bharat Sahayak AI
Government Scheme Model
"""

from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class GovernmentScheme(BaseModel):
    __tablename__ = "government_schemes"

    scheme_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    scheme_name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)

    ministry: Mapped[str | None] = mapped_column(String(255))
    government_level: Mapped[str] = mapped_column(String(30), default="Central")

    state: Mapped[str | None] = mapped_column(String(100))
    district: Mapped[str | None] = mapped_column(String(100))

    category: Mapped[str] = mapped_column(String(100), index=True)

    short_description: Mapped[str | None] = mapped_column(Text)
    detailed_description: Mapped[str | None] = mapped_column(Text)

    eligibility: Mapped[str | None] = mapped_column(Text)
    benefits: Mapped[str | None] = mapped_column(Text)
    required_documents: Mapped[str | None] = mapped_column(Text)

    official_website: Mapped[str | None] = mapped_column(String(500))
    application_link: Mapped[str | None] = mapped_column(String(500))

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)

    tags: Mapped[str | None] = mapped_column(Text)
    keywords: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return (
            f"<GovernmentScheme(id={self.id}, "
            f"name='{self.scheme_name}', "
            f"category='{self.category}')>"
        )
