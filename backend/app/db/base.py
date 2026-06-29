"""
===========================================================
Bharat Sahayak AI
Database Base Configuration
===========================================================
"""

from datetime import datetime
from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy import DateTime


# ===========================================================
# Naming Convention
# ===========================================================

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


metadata = MetaData(
    naming_convention=NAMING_CONVENTION
)


# ===========================================================
# Main Base Class
# ===========================================================

class Base(DeclarativeBase):
    """
    Base class inherited by every SQLAlchemy model.
    """

    metadata = metadata

    __allow_unmapped__ = True


# ===========================================================
# Timestamp Mixin
# ===========================================================

class TimestampMixin:
    """
    Automatically adds:

    - created_at
    - updated_at
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


# ===========================================================
# Primary Key Mixin
# ===========================================================

class PrimaryKeyMixin:
    """
    Auto Increment Integer Primary Key
    """

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
    )


# ===========================================================
# UUID Ready Mixin (Future)
# ===========================================================

class UUIDMixin:
    """
    Reserved for future UUID implementation.

    We are currently using integer IDs because they
    are simpler for development and administration.

    Can be switched to UUID later without changing
    model structure.
    """

    pass


# ===========================================================
# Soft Delete Mixin
# ===========================================================

class SoftDeleteMixin:
    """
    Used by models which require soft deletion.
    """

    is_deleted: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )


# ===========================================================
# Audit Mixin
# ===========================================================

class AuditMixin:
    """
    Keeps track of who created and updated records.
    """

    created_by: Mapped[int | None] = mapped_column(
        nullable=True
    )

    updated_by: Mapped[int | None] = mapped_column(
        nullable=True
    )


# ===========================================================
# Complete Base Model
# ===========================================================

class BaseModel(
    Base,
    PrimaryKeyMixin,
    TimestampMixin,
):
    """
    Every model in Bharat Sahayak AI
    should inherit from BaseModel.
    """

    __abstract__ = True

    def to_dict(self) -> dict[str, Any]:
        """
        Convert SQLAlchemy model into dictionary.
        """

        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):

        values = ", ".join(
            f"{c.name}={getattr(self, c.name)!r}"
            for c in self.__table__.columns
        )

        return f"<{self.__class__.__name__}({values})>"