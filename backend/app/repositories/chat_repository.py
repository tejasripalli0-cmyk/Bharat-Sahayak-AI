"""
Bharat Sahayak AI
Chat Repository

Production-ready repository for chat sessions and messages.
"""

from typing import Optional

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.models.chat import ChatSession, ChatMessage


class ChatRepository:
    def __init__(self, db: Session):
        self.db = db

    # ---------- Chat Sessions ----------

    def create_session(self, session: ChatSession) -> ChatSession:
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_session(self, session_id: int) -> Optional[ChatSession]:
        return (
            self.db.query(ChatSession)
            .filter(ChatSession.id == session_id)
            .first()
        )

    def get_user_sessions(
        self,
        user_id: int,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ChatSession]:
        return (
            self.db.query(ChatSession)
            .filter(ChatSession.user_id == user_id)
            .order_by(desc(ChatSession.created_at))
            .offset(offset)
            .limit(limit)
            .all()
        )

    def rename_session(
        self,
        session: ChatSession,
        title: str,
    ) -> ChatSession:
        session.session_title = title
        self.db.commit()
        self.db.refresh(session)
        return session

    def delete_session(self, session: ChatSession) -> None:
        self.db.delete(session)
        self.db.commit()

    # ---------- Messages ----------

    def add_message(
        self,
        message: ChatMessage,
    ) -> ChatMessage:
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_messages(
        self,
        session_id: int,
        limit: int = 100,
    ) -> list[ChatMessage]:
        return (
            self.db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at)
            .limit(limit)
            .all()
        )

    def latest_message(
        self,
        session_id: int,
    ) -> Optional[ChatMessage]:
        return (
            self.db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(desc(ChatMessage.created_at))
            .first()
        )

    def search_messages(
        self,
        session_id: int,
        keyword: str,
    ) -> list[ChatMessage]:
        return (
            self.db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .filter(ChatMessage.message.ilike(f"%{keyword}%"))
            .all()
        )

    def total_messages(self, session_id: int) -> int:
        return (
            self.db.query(func.count(ChatMessage.id))
            .filter(ChatMessage.session_id == session_id)
            .scalar()
        ) or 0

    def total_tokens(self, session_id: int) -> int:
        return (
            self.db.query(func.sum(ChatMessage.token_usage))
            .filter(ChatMessage.session_id == session_id)
            .scalar()
        ) or 0

    def delete_message(self, message: ChatMessage) -> None:
        self.db.delete(message)
        self.db.commit()
