"""
Bharat Sahayak AI
Routes Package
"""

from app.routes.home import router as home_router
from app.routes.health import router as health_router
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from app.routes.profile import router as profile_router
from app.routes.dashboard import router as dashboard_router

from app.routes.scheme import router as scheme_router
from app.routes.saved_scheme import router as saved_scheme_router
from app.routes.application import router as application_router
from app.routes.eligibility import router as eligibility_router
from app.routes.search import router as search_router

from app.routes.chat import router as chat_router
from app.routes.ai import router as ai_router
from app.routes.rag import router as rag_router
from app.routes.translation import router as translation_router
from app.routes.voice import router as voice_router

from app.routes.notification import router as notification_router
from app.routes.feedback import router as feedback_router
from app.routes.document import router as document_router

from app.routes.upload import router as upload_router
from app.routes.download import router as download_router
from app.routes.import_routes import router as import_router
from app.routes.export import router as export_router
from app.routes.report import router as report_router

from app.routes.admin import router as admin_router
from app.routes.analytics import router as analytics_router
from app.routes.metrics import router as metrics_router
from app.routes.system import router as system_router
from app.routes.system_configuration import (
    router as system_configuration_router,
)
from app.routes.api_key import router as api_key_router
from app.routes.audit import router as audit_router
from app.routes.login_history import router as login_history_router
from app.routes.webhook import router as webhook_router

__all__ = [
    "home_router",
    "health_router",
    "auth_router",
    "user_router",
    "profile_router",
    "dashboard_router",
    "scheme_router",
    "saved_scheme_router",
    "application_router",
    "eligibility_router",
    "search_router",
    "chat_router",
    "ai_router",
    "rag_router",
    "translation_router",
    "voice_router",
    "notification_router",
    "feedback_router",
    "document_router",
    "upload_router",
    "download_router",
    "import_router",
    "export_router",
    "report_router",
    "admin_router",
    "analytics_router",
    "metrics_router",
    "system_router",
    "system_configuration_router",
    "api_key_router",
    "audit_router",
    "login_history_router",
    "webhook_router",
]