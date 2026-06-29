"""
Bharat Sahayak AI
Document Model
"""

from sqlalchemy import String, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    document_type: Mapped[str] = mapped_column(String(100), nullable=False)
    document_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    mime_type: Mapped[str | None] = mapped_column(String(100))
    file_size: Mapped[int | None]
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    remarks: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"<Document(id={self.id}, type='{self.document_type}')>"
