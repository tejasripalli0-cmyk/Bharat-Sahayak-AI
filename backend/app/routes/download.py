"""
Bharat Sahayak AI
Download Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/download",
    tags=["Download"],
)


@router.get("/document/{document_id}")
def download_document(document_id: int):
    return {
        "document_id": document_id,
        "message": "Document download endpoint ready"
    }


@router.get("/report/{report_id}")
def download_report(report_id: int):
    return {
        "report_id": report_id,
        "message": "Report download endpoint ready"
    }
