"""
Bharat Sahayak AI
Document Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/")
def upload_document():
    return {"message": "Document upload endpoint ready"}


@router.get("/{user_id}")
def list_documents(user_id: int):
    return {
        "message": "User documents endpoint ready",
        "user_id": user_id,
    }


@router.put("/{document_id}/verify")
def verify_document(document_id: int):
    return {
        "message": "Document verified",
        "document_id": document_id,
    }


@router.delete("/{document_id}")
def delete_document(document_id: int):
    return {
        "message": "Document deleted",
        "document_id": document_id,
    }
