from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

# Ollama local config
OLLAMA_URL = "http://ollama:11434"
MODEL_NAME = "deepseek-r1:latest"

class PromptRequest(BaseModel):
    prompt: str

@router.post("/summarize")
async def summarize(req: PromptRequest):
    try:
        full_prompt = (
            "You are a helpful assistant. Summarize the following content clearly and concisely:\n\n"
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
        summary = result.get("response", "").strip()

        return {"success": True, "summary": summary}

    except Exception as e:
        return {"success": False, "error": str(e)}
