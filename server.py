from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import router

app = FastAPI(
    title="Embeding Test",
    description="Endpoints to test BERTimbau embedding model with vector retrieval",
    version="0.0.1",
)

app.include_router(router)

