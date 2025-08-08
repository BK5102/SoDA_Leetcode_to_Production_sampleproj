## FastAPI app instance and app startup 

from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Leetcode to Microservice workshop")

app.include_router(api_router)

