import os
from pathlib import Path

from openai import OpenAI
from pydantic import BaseModel, Field

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set")


class CVDetailsExtraction(BaseModel):
    name: str = Field(description="Full name of the candidate.")
    email: str | None = Field(default=None, description="Primary email address if present.")
    phone: str | None = Field(default=None, description="Phone number if present.")
    total_experience_years: float = Field(
        description="Total years of professional work experience, rounded to one decimal place."
    )
    job_titles: list[str] = Field(
        default_factory=list,
        description="List of job titles or roles held by the candidate.",
    )
    skills: list[str] = Field(
        default_factory=list,
        description="Skills or technologies mentioned in the resume.",
    )


client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)


def read_resume_text(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {file_path}")
    return path.read_text(encoding="utf-8")


resume_path = "resume.txt"
resume_text = read_resume_text(resume_path) if Path(resume_path).exists() else """
Ankur Sharma
Software Engineer with 14 years of experience building web apps.
Email: ankur.sharma@email.com
Phone: +91-999-123-4567
Experience:
- Engineering Manager at Tech Corp (2021 - Present)
- Junior Developer at Web Solutions (2018 - 2021)
Skills: Python, FastAPI, JavaScript, React, SQL
"""

completion = client.beta.chat.completions.parse(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Extract the candidate's name, email, phone number, total experience in years, job titles, and skills from the resume text. Return only valid structured data.",
        },
        {"role": "user", "content": resume_text},
    ],
    response_format=CVDetailsExtraction,
)

parsed = completion.choices[0].message.parsed
print(parsed.model_dump_json(indent=2))
