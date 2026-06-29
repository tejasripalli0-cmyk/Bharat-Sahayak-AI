"""
Bharat Sahayak AI
Scheme Service
"""

from sqlalchemy.orm import Session

from app.models.government_scheme import GovernmentScheme
from app.repositories.scheme_repository import SchemeRepository


class SchemeService:
    def __init__(self, db: Session):
        self.db = db
        self.scheme_repository = SchemeRepository(db)

    def create_scheme(self, scheme: GovernmentScheme) -> GovernmentScheme:
        return self.scheme_repository.create(scheme)

    def get_scheme(self, scheme_id: int) -> GovernmentScheme | None:
        return self.scheme_repository.get_by_id(scheme_id)

    def list_schemes(self):
        return self.scheme_repository.list_schemes()

    def search_schemes(self, keyword: str):
        return self.scheme_repository.search(keyword)

    def update_scheme(self, scheme: GovernmentScheme) -> GovernmentScheme:
        return self.scheme_repository.update(scheme)

    def delete_scheme(self, scheme: GovernmentScheme) -> None:
        self.scheme_repository.delete(scheme)
