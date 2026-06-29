"""
Bharat Sahayak AI
Chat Service
"""

from sqlalchemy.orm import Session

from app.models.chat import ChatMessage, ChatSession
from app.repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, db: Session):
        self.db = db
        self.chat_repository = ChatRepository(db)

    def create_session(self, session: ChatSession) -> ChatSession:
        return self.chat_repository.create_session(session)

    def get_session(self, session_id: int):
        return self.chat_repository.get_session(session_id)

    def get_user_sessions(self, user_id: int):
        return self.chat_repository.get_user_sessions(user_id)

    def add_message(self, message: ChatMessage):
        return self.chat_repository.add_message(message)

    def get_messages(self, session_id: int):
        return self.chat_repository.get_messages(session_id)

    def search_messages(self, session_id: int, keyword: str):
        return self.chat_repository.search_messages(session_id, keyword)

    def total_messages(self, session_id: int):
        return self.chat_repository.total_messages(session_id)

    def total_tokens(self, session_id: int):
        return self.chat_repository.total_tokens(session_id)

    def delete_session(self, session: ChatSession):
        self.chat_repository.delete_session(session)
