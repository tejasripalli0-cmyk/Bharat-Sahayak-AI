"""
Bharat Sahayak AI
Audit Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/audit",
    tags=["Audit"],
)


@router.get("/")
def list_audit_logs():
    return {
        "message": "Audit logs endpoint ready"
    }


@router.get("/{log_id}")
def get_audit_log(log_id: int):
    return {
        "message": "Audit log details",
        "log_id": log_id,
    }


@router.delete("/{log_id}")
def delete_audit_log(log_id: int):
    return {
        "message": "Audit log deleted",
        "log_id": log_id,
    }