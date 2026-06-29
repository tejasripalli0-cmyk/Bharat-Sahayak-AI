"""
Bharat Sahayak AI
Eligibility Schemas
"""

from pydantic import BaseModel, Field


class EligibilityRequest(BaseModel):
    """
    Dynamic eligibility request.

    The frontend will display additional fields depending on the
    occupations selected by the user.
    """

    # ---------------------------------------------------------
    # Language
    # ---------------------------------------------------------
    language: str = Field(
        default="en",
        description="Preferred response language",
    )

    # ---------------------------------------------------------
    # Personal Information
    # ---------------------------------------------------------
    first_name: str
    age: int
    gender: str

    # ---------------------------------------------------------
    # Address
    # ---------------------------------------------------------
    state: str
    district: str

    # ---------------------------------------------------------
    # Financial
    # ---------------------------------------------------------
    annual_income: float
    category: str

    # ---------------------------------------------------------
    # Multiple Occupations
    # Examples:
    # ["Student"]
    # ["Farmer", "Student"]
    # ["Senior Citizen", "Widow"]
    # ---------------------------------------------------------
    occupations: list[str] = []

    # ---------------------------------------------------------
    # Student Details
    # ---------------------------------------------------------
    education_level: str | None = None
    course: str | None = None
    college_name: str | None = None
    year_of_study: int | None = None

    # ---------------------------------------------------------
    # Farmer Details
    # ---------------------------------------------------------
    land_area: float | None = None
    crop_type: str | None = None
    irrigation_type: str | None = None
    farmer_id: str | None = None

    # ---------------------------------------------------------
    # Worker Details
    # ---------------------------------------------------------
    labour_card_number: str | None = None
    employer_name: str | None = None
    monthly_salary: float | None = None

    # ---------------------------------------------------------
    # Senior Citizen
    # ---------------------------------------------------------
    pensioner: bool = False
    pension_amount: float | None = None
    living_alone: bool = False

    # ---------------------------------------------------------
    # Widow
    # ---------------------------------------------------------
    dependent_children: int | None = None
    widow_pension: bool = False

    # ---------------------------------------------------------
    # Disability
    # ---------------------------------------------------------
    disability: bool = False
    disability_percentage: float | None = None
    disability_certificate_number: str | None = None

    # ---------------------------------------------------------
    # Other Categories
    # ---------------------------------------------------------
    minority: bool = False
    ex_serviceman: bool = False
    orphan: bool = False
    self_employed: bool = False


class SchemeRecommendation(BaseModel):
    """
    AI recommendation response.
    """

    id: int
    name: str
    category: str

    reason: str

    benefits: str | None = None

    required_documents: list[str] = []

    application_url: str | None = None

    official_website: str | None = None

    language: str = "en"