from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router  # 👈 import router

# Create tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Include routes.py
app.include_router(router)
