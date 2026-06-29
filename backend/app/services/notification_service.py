"""
Bharat Sahayak AI
Notification Service
"""

from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.repositories.notification_repository import NotificationRepository


class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        self.notification_repository = NotificationRepository(db)

    def create_notification(self, notification: Notification) -> Notification:
        return self.notification_repository.create(notification)

    def get_notifications(self, user_id: int):
        return self.notification_repository.get_user_notifications(user_id)

    def get_unread_notifications(self, user_id: int):
        return self.notification_repository.get_user_notifications(
            user_id=user_id,
            unread_only=True,
        )

    def mark_as_read(self, notification: Notification):
        return self.notification_repository.mark_as_read(notification)

    def mark_all_as_read(self, user_id: int):
        return self.notification_repository.mark_all_as_read(user_id)

    def unread_count(self, user_id: int):
        return self.notification_repository.unread_count(user_id)
