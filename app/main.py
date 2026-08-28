from fastapi import FastAPI
from app.api.controllers.image_quality_controller import router

app = FastAPI()
app.include_router(router)