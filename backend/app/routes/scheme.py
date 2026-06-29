"""
Bharat Sahayak AI
Scheme Router
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.scheme import Scheme
from app.repositories.scheme_repository import SchemeRepository
from app.schemas.scheme import CreateSchemeRequest

router = APIRouter(
    prefix="/schemes",
    tags=["Schemes"],
)


@router.get("/")
def list_schemes(
    db: Session = Depends(get_db),
):
    repository = SchemeRepository(db)

    schemes = repository.list_schemes()

    return [
        {
            "id": scheme.id,
            "name": scheme.name,
            "category": scheme.category,
            "ministry": scheme.ministry,
            "state": scheme.state,
            "description": scheme.description,
            "eligibility": scheme.eligibility,
            "benefits": scheme.benefits,
            "application_url": scheme.application_url,
            "income_limit": scheme.income_limit,
            "is_active": scheme.is_active,
        }
        for scheme in schemes
    ]


@router.get("/{scheme_id}")
def get_scheme(
    scheme_id: int,
    db: Session = Depends(get_db),
):
    repository = SchemeRepository(db)

    scheme = repository.get_by_id(scheme_id)

    if scheme is None:
        return {
            "message": "Scheme not found",
        }

    return {
        "id": scheme.id,
        "name": scheme.name,
        "category": scheme.category,
        "ministry": scheme.ministry,
        "state": scheme.state,
        "description": scheme.description,
        "eligibility": scheme.eligibility,
        "benefits": scheme.benefits,
        "application_url": scheme.application_url,
        "income_limit": scheme.income_limit,
        "is_active": scheme.is_active,
    }


@router.post("/")
def create_scheme(
    request: CreateSchemeRequest,
    db: Session = Depends(get_db),
):
    repository = SchemeRepository(db)

    scheme = Scheme(
        name=request.name,
        category=request.category,
        ministry=request.ministry,
        state=request.state,
        description=request.description,
        eligibility=request.eligibility,
        benefits=request.benefits,
        application_url=request.application_url,
        income_limit=request.income_limit,
    )

    repository.create(scheme)

    return {
        "message": "Scheme created successfully",
        "scheme_id": scheme.id,
        "name": scheme.name,
    }


@router.put("/{scheme_id}")
def update_scheme(
    scheme_id: int,
):
    return {
        "message": "Update scheme endpoint will be implemented later",
        "scheme_id": scheme_id,
    }


@router.delete("/{scheme_id}")
def delete_scheme(
    scheme_id: int,
):
    return {
        "message": "Delete scheme endpoint will be implemented later",
        "scheme_id": scheme_id,
    }