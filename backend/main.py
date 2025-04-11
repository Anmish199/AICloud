from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InfraRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_infra(request: InfraRequest):
    openai.api_key = "your-openai-key"  # Replace with your real key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate Terraform for: {request.prompt}",
        max_tokens=500
    )
    return {"code": response["choices"][0]["text"]}
