from fastapi import APIRouter

from .retriever_route import route as RetrieverRoute

routes_router = APIRouter(
    prefix="/retrieval",
)

routes_router.include_router(RetrieverRoute)