from fastapi import FastAPI
from app.routes import embed

app = FastAPI()

# Include embed router
app.include_router(embed.router, prefix="/embed")
