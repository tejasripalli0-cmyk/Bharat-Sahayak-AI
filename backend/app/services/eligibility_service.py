"""
Bharat Sahayak AI
Eligibility Service
"""

from app.models.scheme import Scheme
from app.schemas.eligibility import EligibilityRequest


class EligibilityService:
    """
    Handles government scheme eligibility matching.
    """

    def get_matching_schemes(
        self,
        request: EligibilityRequest,
        schemes: list[Scheme],
    ) -> list[Scheme]:

        matching = []

        for scheme in schemes:

            # Skip inactive schemes
            if not scheme.is_active:
                continue

            # ----------------------------
            # State Check
            # ----------------------------
            if (
                scheme.state
                and scheme.state != "All India"
                and scheme.state.lower() != request.state.lower()
            ):
                continue

            # ----------------------------
            # Income Check
            # ----------------------------
            if (
                scheme.income_limit is not None
                and request.annual_income > scheme.income_limit
            ):
                continue

            # ----------------------------
            # Gender Check
            # ----------------------------
            if (
                scheme.gender
                and scheme.gender.lower() != "all"
                and scheme.gender.lower() != request.gender.lower()
            ):
                continue

            # ----------------------------
            # Age Check
            # ----------------------------
            if (
                scheme.minimum_age is not None
                and request.age < scheme.minimum_age
            ):
                continue

            if (
                scheme.maximum_age is not None
                and request.age > scheme.maximum_age
            ):
                continue

            # ----------------------------
            # Occupation Check
            # ----------------------------
            if scheme.occupation:

                user_occupations = [
                    occupation.lower()
                    for occupation in request.occupations
                ]

                if scheme.occupation.lower() not in user_occupations:
                    continue

            matching.append(scheme)

        return matching