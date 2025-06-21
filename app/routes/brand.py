from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

OLLAMA_URL = "http://ollama:11434"  # Use "ollama" if using Docker Compose
MODEL_NAME = "deepseek-r1:latest"

class PromptRequest(BaseModel):
    prompt: str

@router.post("/resume")
async def generate_resume_bullets(req: PromptRequest):
    try:
        full_prompt = (
            "You are a senior technical resume writer. "
            "Based on the input, write clear and concise resume bullet points:\n\n"
            f"{req.prompt}"
        )

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "temperature": 0.7,
                "max_tokens": 1400
            }
        )

        response.raise_for_status()
        data = response.json()
        content = data.get("response", "")

        # Extract bullet points from response
        lines = content.strip().split("\n")
        bullets = [
            line.strip("-•*1234567890. ").strip()
            for line in lines
            if line.strip() and (line.lstrip().startswith(("-", "•")) or line.strip()[0].isdigit())
        ]

        return {"bullets": bullets}

    except Exception as e:
        return {"error": str(e)}
