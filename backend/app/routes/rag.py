"""
Bharat Sahayak AI
RAG Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.post("/index")
def index_documents():
    return {
        "message": "Document indexing endpoint ready"
    }


@router.post("/retrieve")
def retrieve():
    return {
        "message": "Document retrieval endpoint ready"
    }


@router.post("/answer")
def answer():
    return {
        "message": "RAG answer endpoint ready"
    }
