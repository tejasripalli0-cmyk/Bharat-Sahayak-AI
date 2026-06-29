"""
Bharat Sahayak AI
Audit Repository
"""

from typing import Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, log: AuditLog) -> AuditLog:
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    def get_by_id(self, log_id: int) -> Optional[AuditLog]:
        return self.db.query(AuditLog).filter(AuditLog.id == log_id).first()

    def list_logs(self, limit: int = 100):
        return (
            self.db.query(AuditLog)
            .order_by(desc(AuditLog.created_at))
            .limit(limit)
            .all()
        )

    def get_user_logs(self, user_id: int):
        return (
            self.db.query(AuditLog)
            .filter(AuditLog.user_id == user_id)
            .order_by(desc(AuditLog.created_at))
            .all()
        )

    def get_action_logs(self, action: str):
        return (
            self.db.query(AuditLog)
            .filter(AuditLog.action == action)
            .all()
        )

    def delete(self, log: AuditLog):
        self.db.delete(log)
        self.db.commit()
