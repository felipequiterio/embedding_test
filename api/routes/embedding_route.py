from fastapi import FastAPI, APIRouter

from services.embeddings import get_embeddings

app = FastAPI()

route = APIRouter(
    tags=["Embedding Generation"]
)


@route.post('/generate_embeddings')
async def generate_embeddings(text: str):
    embeddings = get_embeddings(text)
    return {'message': 'Embeddings generated successfully!', 'Embeddings': embeddings}
