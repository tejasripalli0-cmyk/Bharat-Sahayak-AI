"""
Bharat Sahayak AI
Scheme Schemas
"""

from pydantic import BaseModel, Field


class CreateSchemeRequest(BaseModel):
    """
    Create a new government scheme.
    """

    # ---------------------------------------------------------
    # Basic Information
    # ---------------------------------------------------------

    name: str

    category: str

    ministry: str | None = None

    state: str = "All India"

    description: str

    # ---------------------------------------------------------
    # Eligibility Rules
    # ---------------------------------------------------------

    minimum_age: int | None = Field(default=None)

    maximum_age: int | None = Field(default=None)

    gender: str | None = Field(
        default="All",
        description="Male / Female / Other / All",
    )

    occupation: str | None = None

    education_level: str | None = None

    category_allowed: str | None = None

    income_limit: float | None = Field(
        default=None,
        description="Annual income limit in Indian Rupees",
    )

    eligibility: str | None = None

    # ---------------------------------------------------------
    # Benefits
    # ---------------------------------------------------------

    benefits: str | None = None

    benefit_amount: str | None = None

    # ---------------------------------------------------------
    # Documents
    # ---------------------------------------------------------

    required_documents: str | None = None

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    official_website: str | None = None

    application_url: str | None = None

    application_deadline: str | None = None

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    is_active: bool = True


class SchemeResponse(BaseModel):
    """
    Scheme response.
    """

    id: int

    name: str

    category: str

    ministry: str | None

    state: str | None

    minimum_age: int | None

    maximum_age: int | None

    gender: str | None

    occupation: str | None

    education_level: str | None

    category_allowed: str | None

    income_limit: float | None

    benefits: str | None

    benefit_amount: str | None

    required_documents: str | None

    official_website: str | None

    application_url: str | None

    application_deadline: str | None

    is_active: bool

    class Config:
        from_attributes = True