from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_load

app = FastAPI()

class Applicant(BaseModel):
    income :float
    age : int
    employement_status: str


@app.post('/loag_eligibility')
def check_eligibility(applicant : Applicant):
    eligibility = is_eligible_for_load(
        income=applicant.income,
        age = applicant.age,
        employement_status=applicant.employement_status
    )
    return{'eligible' : eligibility}
    