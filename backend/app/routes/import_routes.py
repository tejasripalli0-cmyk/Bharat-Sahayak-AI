"""
Bharat Sahayak AI
Import Router
"""

from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/import",
    tags=["Import"],
)


@router.post("/schemes")
async def import_schemes(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Scheme import endpoint ready"
    }


@router.post("/users")
async def import_users(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "User import endpoint ready"
    }


@router.post("/documents")
async def import_documents(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Document import endpoint ready"
    }
