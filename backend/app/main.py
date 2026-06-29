from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings

# Routers
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
from app.routes.system_configuration import router as system_configuration_router
from app.routes.api_key import router as api_key_router
from app.routes.audit import router as audit_router
from app.routes.login_history import router as login_history_router
from app.routes.webhook import router as webhook_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Bharat Sahayak AI Backend...")
    yield
    print("🛑 Shutting down Bharat Sahayak AI Backend...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Endpoints
app.include_router(home_router)
app.include_router(health_router)

# Authentication
app.include_router(auth_router)

# Users
app.include_router(user_router)
app.include_router(profile_router)
app.include_router(login_history_router)
app.include_router(api_key_router)

# Dashboard
app.include_router(dashboard_router)
app.include_router(metrics_router)
app.include_router(analytics_router)

# Schemes
app.include_router(scheme_router)
app.include_router(saved_scheme_router)
app.include_router(application_router)
app.include_router(search_router)
app.include_router(eligibility_router)

# AI
app.include_router(chat_router)
app.include_router(ai_router)
app.include_router(rag_router)
app.include_router(translation_router)
app.include_router(voice_router)

# Notifications & Documents
app.include_router(notification_router)
app.include_router(feedback_router)
app.include_router(document_router)

# Upload / Download
app.include_router(upload_router)
app.include_router(download_router)
app.include_router(import_router)
app.include_router(export_router)
app.include_router(report_router)

# Admin
app.include_router(admin_router)
app.include_router(system_router)
app.include_router(system_configuration_router)
app.include_router(audit_router)
app.include_router(webhook_router)

@app.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "status": "running",
        "message": "Welcome to Bharat Sahayak AI",
    }

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
    }