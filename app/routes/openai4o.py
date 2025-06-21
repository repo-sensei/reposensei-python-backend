from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

# Ollama local model config
OLLAMA_URL = "http://ollama:11434"
MODEL_NAME = "deepseek-r1:latest"

# Input schema
class PromptRequest(BaseModel):
    prompt: str

# /generate-architecture endpoint
@router.post("/generate-architecture")
async def generate_architecture(req: PromptRequest):
    try:
        full_prompt = (
            "You are a helpful assistant. Generate a system architecture based on the following input:\n\n"
            f"{req.prompt}"
        )

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "temperature": 1.0,
                "top_p": 1.0,
                "max_tokens": 1000,
            }
        )

        response.raise_for_status()
        result = response.json()
        return {"success": True, "response": result.get("response", "").strip()}

    except Exception as e:
        return {"success": False, "error": str(e)}

# /onboard endpoint
@router.post("/onboard")
async def generate_summary(req: PromptRequest):
    try:
        full_prompt = (
            "You are a helpful assistant. Answer clearly and concisely based on the following onboarding content:\n\n"
            f"{req.prompt}"
        )

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "temperature": 0.7,
                "top_p": 1.0,
                "max_tokens": 800,
            }
        )

        response.raise_for_status()
        result = response.json()
        return {"success": True, "summary": result.get("response", "").strip()}

    except Exception as e:
        return {"success": False, "error": str(e)}
