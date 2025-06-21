from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

# Local Ollama endpoint
OLLAMA_URL = "http://ollama:11434"
MODEL_NAME = "deepseek-r1:latest"

class AnalyzePrompt(BaseModel):
    prompt: str

@router.post("/analyze")
async def analyze(req: AnalyzePrompt):
    try:
        full_prompt = (
            "You are a code analysis expert. Analyze the following code and suggest improvements:\n\n"
            f"{req.prompt}"
        )

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "temperature": 0.7,
                "top_p": 1.0,
                "max_tokens": 800
            }
        )

        response.raise_for_status()
        result = response.json()
        content = result.get("response", "").strip()

        return {
            "success": True,
            "suggestions": content or "No meaningful content returned."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
