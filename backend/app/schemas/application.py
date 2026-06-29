"""
Bharat Sahayak AI
Application Schemas
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    user_id: int
    scheme_id: int


class ApplicationUpdate(BaseModel):
    application_status: str
    remarks: str | None = None


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    scheme_id: int
    application_status: str
    application_reference: str | None = None
    remarks: str | None = None
    created_at: datetime
    updated_at: datetime
