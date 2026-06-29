"""
Bharat Sahayak AI
Saved Scheme Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/saved-schemes",
    tags=["Saved Schemes"],
)


@router.get("/{user_id}")
def list_saved(user_id: int):
    return {
        "message": "Saved schemes",
        "user_id": user_id,
    }


@router.post("/{scheme_id}")
def save_scheme(scheme_id: int):
    return {
        "message": "Scheme saved",
        "scheme_id": scheme_id,
    }


@router.delete("/{scheme_id}")
def remove_scheme(scheme_id: int):
    return {
        "message": "Scheme removed",
        "scheme_id": scheme_id,
    }