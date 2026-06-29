"""
Bharat Sahayak AI
API Key Schemas
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class APIKeyCreate(BaseModel):
    name: str
    expires_at: datetime | None = None


class APIKeyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    key_prefix: str
    is_active: bool
    expires_at: datetime | None = None
    created_at: datetime
