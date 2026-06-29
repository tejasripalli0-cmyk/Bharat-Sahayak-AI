from enum import Enum


# ==============================================================================
# 1. USER & AUTHENTICATION
# ==============================================================================

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
    GUEST = "guest"


class AuthProvider(str, Enum):
    LOCAL = "local"         # Password-based
    GOOGLE = "google"
    DIGILOCKER = "digilocker"
    AADHAAR = "aadhaar"     # OTP-based Aadhaar auth
    MOBILE_OTP = "mobile_otp"


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"
    TRANSGENDER = "T"
    PREFER_NOT_TO_SAY = "O"


# ==============================================================================
# 2. LOCALIZATION & GEOGRAPHY
# ==============================================================================

class SupportedLanguage(str, Enum):
    """English + 22 Scheduled Languages of India"""
    ENGLISH = "en"
    ASSAMESE = "as"
    BENGALI = "bn"
    BODO = "brx"
    DOGRI = "doi"
    GUJARATI = "gu"
    HINDI = "hi"
    KANNADA = "kn"
    KASHMIRI = "ks"
    KONKANI = "kok"
    MAITHILI = "mai"
    MALAYALAM = "ml"
    MANIPURI = "mni"
    MARATHI = "mr"
    NEPALI = "ne"
    ODIA = "or"
    PUNJABI = "pa"
    SANSKRIT = "sa"
    SANTALI = "sat"
    SINDHI = "sd"
    TAMIL = "ta"
    TELUGU = "te"
    URDU = "ur"


class IndianStateUT(str, Enum):
    """All 28 States and 8 Union Territories"""
    # States
    ANDHRA_PRADESH = "AP"
    ARUNACHAL_PRADESH = "AR"
    ASSAM = "AS"
    BIHAR = "BR"
    CHHATTISGARH = "CG"
    GOA = "GA"
    GUJARAT = "GJ"
    HARYANA = "HR"
    HIMACHAL_PRADESH = "HP"
    JHARKHAND = "JH"
    KARNATAKA = "KA"
    KERALA = "KL"
    MADHYA_PRADESH = "MP"
    MAHARASHTRA = "MH"
    MANIPUR = "MN"
    MEGHALAYA = "ML"
    MIZORAM = "MZ"
    NAGALAND = "NL"
    ODISHA = "OD"
    PUNJABI = "PB"
    RAJASTHAN = "RJ"
    SIKKIM = "SK"
    TAMIL_NADU = "TN"
    TELANGANA = "TG"
    TRIPURA = "TR"
    UTTAR_PRADESH = "UP"
    UTTARAKHAND = "UK"
    WEST_BENGAL = "WB"
    # Union Territories
    ANDAMAN_NICOBAR = "AN"
    CHANDIGARH = "CH"
    DADRA_NAGAR_HAVELI_DAMAN_DIU = "DN"
    DELHI = "DL"
    JAMMU_KASHMIR = "JK"
    LADAKH = "LA"
    LAKSHADWEEP = "LD"
    PUDUCHERRY = "PY"


# ==============================================================================
# 3. SCHEMES & ELIGIBILITY
# ==============================================================================

class SchemeCategory(str, Enum):
    AGRICULTURE = "Agriculture"
    EDUCATION = "Education"
    HEALTH = "Health"
    EMPLOYMENT = "Employment"
    WOMEN = "Women"
    STUDENTS = "Students"
    HOUSING = "Housing"
    PENSION = "Pension"
    BUSINESS = "Business"
    SKILL_DEVELOPMENT = "Skill Development"
    SOCIAL_WELFARE = "Social Welfare"
    MINORITIES = "Minorities"
    DIRTY_UTILITIES = "Utility & Infrastructure"


class SchemeStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
    DRAFT = "draft"


class EligibilityStatus(str, Enum):
    ELIGIBLE = "eligible"
    INELIGIBLE = "ineligible"
    CONDITIONALLY_ELIGIBLE = "conditionally_eligible"
    NEED_MORE_INFO = "need_more_info"


class GovernmentLevel(str, Enum):
    CENTRAL = "central"
    STATE = "state"
    DISTRICT = "district"
    LOCAL_BODY = "local_body"  # Panchayat / Municipal


# ==============================================================================
# 4. CHAT, AI, & VOICE ARCHITECTURE
# ==============================================================================

class ChatRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class AIProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    GROQ = "groq"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"


class VoiceProvider(str, Enum):
    AZURE = "azure"
    GOOGLE_TTS = "google_tts"
    ELEVENLABS = "elevenlabs"
    BHASHINI = "bhashini"     # Highly relevant for Indian languages
    SARVAM_AI = "sarvam_ai"


# ==============================================================================
# 5. DOCUMENTS, UPLOADS, & NOTIFICATIONS
# ==============================================================================

class DocumentType(str, Enum):
    AADHAAR = "aadhaar_card"
    PAN = "pan_card"
    VOTER_ID = "voter_id"
    RATION_CARD = "ration_card"
    INCOME_CERTIFICATE = "income_certificate"
    CASTE_CERTIFICATE = "caste_certificate"
    RESIDENCE_PROOF = "residence_proof"
    MARKSHEET = "educational_marksheet"


class UploadType(str, Enum):
    PROFILE_PICTURE = "profile_picture"
    DOCUMENT_PROOF = "document_proof"
    CHAT_ATTACHMENT = "chat_attachment"
    SCHEME_BANNER = "scheme_banner"
    BULK_DATA_IMPORT = "bulk_data_import"


class NotificationType(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    IN_APP = "in_app"
    PUSH = "push"


# ==============================================================================
# 6. SYSTEM, NETWORKING & APP METADATA (Global Constants)
# ==============================================================================

class HTTPMessage:
    SUCCESS = "Operation completed successfully."
    BAD_REQUEST = "Invalid input or missing required parameters."
    UNAUTHORIZED = "Authentication credentials are missing or invalid."
    FORBIDDEN = "You do not have permission to access this resource."
    NOT_FOUND = "The requested resource could not be found."
    INTERNAL_SERVER_ERROR = "An unexpected error occurred on the server."


class PaginationConstants:
    DEFAULT_PAGE = 1
    DEFAULT_LIMIT = 20
    MAX_LIMIT = 100


class PasswordPolicy:
    MIN_LENGTH = 8
    MAX_LENGTH = 64
    REQUIRE_UPPERCASE = True
    REQUIRE_LOWERCASE = True
    REQUIRE_NUMBERS = True
    REQUIRE_SPECIAL_CHAR = True


class DateTimeFormat:
    ISO_8601 = "%Y-%m-%dT%H:%M:%S.%fZ"
    DB_DATE = "%Y-%m-%d"
    DB_DATETIME = "%Y-%m-%d %H:%M:%S"
    DISPLAY_DATE = "%d-%m-%Y"
    DISPLAY_DATETIME = "%d-%m-%Y %I:%M %p"


class APIConstants:
    VERSION_V1 = "/api/v1"
    VERSION_V2 = "/api/v2"
    TIMEOUT_SECONDS = 30
    MAX_RETRIES = 3


class ApplicationMetadata:
    APP_NAME = "Jan Kalyan Scheme Portal"
    VERSION = "1.0.0"
    ENVIRONMENT_DEVELOPMENT = "development"
    ENVIRONMENT_STAGING = "staging"
    ENVIRONMENT_PRODUCTION = "production"