"""
Bharat Sahayak AI
Notification Repository
"""

from typing import Optional

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.models.notification import Notification


class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, notification: Notification) -> Notification:
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def get_by_id(self, notification_id: int) -> Optional[Notification]:
        return (
            self.db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

    def get_user_notifications(
        self,
        user_id: int,
        limit: int = 100,
        offset: int = 0,
        unread_only: bool = False,
    ) -> list[Notification]:
        query = (
            self.db.query(Notification)
            .filter(Notification.user_id == user_id)
        )
        if unread_only:
            query = query.filter(Notification.is_read.is_(False))
        return (
            query.order_by(desc(Notification.created_at))
            .offset(offset)
            .limit(limit)
            .all()
        )

    def mark_as_read(self, notification: Notification) -> Notification:
        notification.is_read = True
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def mark_all_as_read(self, user_id: int) -> int:
        updated = (
            self.db.query(Notification)
            .filter(Notification.user_id == user_id)
            .filter(Notification.is_read.is_(False))
            .update({"is_read": True})
        )
        self.db.commit()
        return updated

    def unread_count(self, user_id: int) -> int:
        return (
            self.db.query(func.count(Notification.id))
            .filter(Notification.user_id == user_id)
            .filter(Notification.is_read.is_(False))
            .scalar()
        ) or 0

    def delete(self, notification: Notification) -> None:
        self.db.delete(notification)
        self.db.commit()
