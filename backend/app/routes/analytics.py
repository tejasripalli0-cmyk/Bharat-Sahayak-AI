"""
Bharat Sahayak AI
Analytics Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/dashboard")
def dashboard():
    return {"message": "Analytics dashboard endpoint ready"}


@router.get("/usage")
def usage():
    return {"message": "Usage analytics endpoint ready"}


@router.get("/performance")
def performance():
    return {"message": "Performance analytics endpoint ready"}


@router.get("/reports")
def reports():
    return {"message": "Reports endpoint ready"}
