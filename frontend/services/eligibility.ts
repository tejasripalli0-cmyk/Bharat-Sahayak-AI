import { apiRequest } from "./api";

/*
=========================================
Bharat Sahayak AI
Eligibility Service
=========================================
*/

export interface EligibilityRequest {
  language: string;

  first_name: string;
  age: number;
  gender: string;

  state: string;
  district: string;

  annual_income: number;
  category: string;

  occupations: string[];

  // Student
  education_level?: string;
  course?: string;
  college_name?: string;
  year_of_study?: number;

  // Farmer
  land_area?: number;
  crop_type?: string;
  irrigation_type?: string;
  farmer_id?: string;

  // Worker
  labour_card_number?: string;
  employer_name?: string;
  monthly_salary?: number;

  // Senior Citizen
  pensioner?: boolean;
  pension_amount?: number;
  living_alone?: boolean;

  // Widow
  dependent_children?: number;
  widow_pension?: boolean;

  // Disability
  disability?: boolean;
  disability_percentage?: number;
  disability_certificate_number?: string;

  // Other
  minority?: boolean;
  ex_serviceman?: boolean;
  orphan?: boolean;
  self_employed?: boolean;
}

export async function checkEligibility(
  data: EligibilityRequest
) {
  return await apiRequest(
    "/eligibility/check",
    "POST",
    data
  );
}

export async function getRecommendations(
  userId: number
) {
  return await apiRequest(
    `/eligibility/recommendations/${userId}`,
    "GET"
  );
}

export async function getEligibilityScore(
  userId: number,
  schemeId: number
) {
  return await apiRequest(
    `/eligibility/score/${userId}/${schemeId}`,
    "GET"
  );
}