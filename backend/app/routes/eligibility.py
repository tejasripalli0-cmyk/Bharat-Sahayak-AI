"""
Bharat Sahayak AI
Eligibility Router
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.scheme_repository import SchemeRepository
from app.schemas.eligibility import EligibilityRequest
from app.services.eligibility_service import EligibilityService

router = APIRouter(
    prefix="/eligibility",
    tags=["Eligibility"],
)

eligibility_service = EligibilityService()


@router.post("/check")
def check_eligibility(
    request: EligibilityRequest,
    db: Session = Depends(get_db),
):
    """
    Check user eligibility for government schemes.
    """

    repository = SchemeRepository(db)

    all_schemes = repository.list_schemes()

    matching_schemes = eligibility_service.get_matching_schemes(
        request=request,
        schemes=all_schemes,
    )

    return {
        "language": request.language,
        "user_profile": {
            "name": request.first_name,
            "age": request.age,
            "gender": request.gender,
            "state": request.state,
            "district": request.district,
            "annual_income": request.annual_income,
            "category": request.category,
            "occupations": request.occupations,
        },
        "total_schemes": len(all_schemes),
        "eligible_schemes": len(matching_schemes),
        "matching_schemes": [
            {
                "id": scheme.id,
                "name": scheme.name,
                "category": scheme.category,
                "state": scheme.state,
                "benefits": scheme.benefits,
                "application_url": scheme.application_url,
            }
            for scheme in matching_schemes
        ],
        "message": "Eligibility check completed successfully."
    }


@router.get("/recommendations/{user_id}")
def recommend_schemes(user_id: int):
    return {
        "message": "AI recommendations will be available soon.",
        "user_id": user_id,
    }


@router.get("/score/{user_id}/{scheme_id}")
def eligibility_score(
    user_id: int,
    scheme_id: int,
):
    return {
        "message": "Eligibility scoring will be implemented later.",
        "user_id": user_id,
        "scheme_id": scheme_id,
    }