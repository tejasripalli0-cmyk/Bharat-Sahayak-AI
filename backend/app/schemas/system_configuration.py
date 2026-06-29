"""
Bharat Sahayak AI
System Configuration Model
"""

from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class SystemConfiguration(BaseModel):
    __tablename__ = "system_configuration"

    config_key: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
        nullable=False,
    )

    config_value: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(Text)

    is_editable: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<SystemConfiguration(key='{self.config_key}')>"
