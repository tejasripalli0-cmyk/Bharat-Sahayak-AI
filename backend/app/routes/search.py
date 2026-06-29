"""
Bharat Sahayak AI
Search Router
"""

from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get("/schemes")
def search_schemes(
    q: str = Query(..., description="Search keyword")
):
    return {
        "message": "Scheme search endpoint ready",
        "query": q,
    }


@router.get("/global")
def global_search(
    q: str = Query(..., description="Global search keyword")
):
    return {
        "message": "Global search endpoint ready",
        "query": q,
    }


@router.get("/categories")
def categories():
    return {
        "message": "Scheme categories endpoint ready"
    }


@router.get("/states")
def states():
    return {
        "message": "States endpoint ready"
    }
