"""
Bharat Sahayak AI
Document Repository
"""

from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_by_id(self, document_id: int) -> Optional[Document]:
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_user_documents(
        self,
        user_id: int,
        verified_only: bool = False,
    ) -> list[Document]:
        query = (
            self.db.query(Document)
            .filter(Document.user_id == user_id)
        )

        if verified_only:
            query = query.filter(Document.is_verified.is_(True))

        return query.order_by(desc(Document.created_at)).all()

    def verify(self, document: Document) -> Document:
        document.is_verified = True
        self.db.commit()
        self.db.refresh(document)
        return document

    def update(self, document: Document) -> Document:
        self.db.commit()
        self.db.refresh(document)
        return document

    def delete(self, document: Document) -> None:
        self.db.delete(document)
        self.db.commit()
