from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import predict_job

app = FastAPI()

# Allow your React frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what data the frontend will send
class JobPosting(BaseModel):
    text: str
    telecommuting: int
    has_logo: int
    has_questions: int
    employment_type: str
    experience: str
    education: str

@app.post("/predict")
def predict(job: JobPosting):
    result = predict_job(
        text=job.text,
        telecommuting=job.telecommuting,
        has_logo=job.has_logo,
        has_questions=job.has_questions,
        employment_type=job.employment_type,
        experience=job.experience,
        education=job.education
    )
    return result