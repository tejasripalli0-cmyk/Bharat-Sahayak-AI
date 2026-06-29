"""
Bharat Sahayak AI
Scheme Repository
"""

from sqlalchemy.orm import Session

from app.models.scheme import Scheme


class SchemeRepository:

    def __init__(self, db: Session):
        self.db = db

    def list_schemes(self):
        return (
            self.db.query(Scheme)
            .order_by(Scheme.created_at.desc())
            .all()
        )

    def get_by_id(self, scheme_id: int):
        return (
            self.db.query(Scheme)
            .filter(Scheme.id == scheme_id)
            .first()
        )

    def create(self, scheme: Scheme):
        self.db.add(scheme)
        self.db.commit()
        self.db.refresh(scheme)
        return scheme

    def update(self, scheme: Scheme):
        self.db.commit()
        self.db.refresh(scheme)
        return scheme

    def delete(self, scheme: Scheme):
        self.db.delete(scheme)
        self.db.commit()
