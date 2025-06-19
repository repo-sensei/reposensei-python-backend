from fastapi import FastAPI
from app.routes import commit
from app.routes import embed
from app.routes import openai4o
from app.routes import hotspot
from app.routes import brand

app = FastAPI()

# Include embed router
app.include_router(brand.router)
app.include_router(hotspot.router)
app.include_router(commit.router)
app.include_router(embed.router, prefix="/embed")
app.include_router(openai4o.router)


