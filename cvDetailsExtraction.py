import json
from pydantic import BaseModel, Field
from openai import OpenAI
import os

# 1. Define the desired output structure using Pydantic
class cvDetailsExtraction(BaseModel):
    name: str = Field(description="The full name of the candidate.")
    total_experience_years: float = Field(description="Total years of professional work experience.")
    job_titles: list[str] = Field(description="List of job titles held by the candidate.")

# 2. Initialize the OpenAI client
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set")

client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

# 3. Sample resume text
resume_text = """
Jane Doe
Software Engineer with 5.5 years of experience building web apps.
Experience:
- Senior Developer at Tech Corp (2021 - Present)
- Junior Developer at Web Solutions (2018 - 2021)
"""

# 4. Call the model using Pydantic beta parsing
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the requested information from the resume."},
        {"role": "user", "content": resume_text},
    ],
    response_format=cvDetailsExtraction,
)

# 5. Get the parsed Pydantic object and convert it to JSON
extracted_data = completion.choices[0].message.parsed
json_output = extracted_data.model_dump_json(indent=2)

print(json_output)
