from fastapi import APIRouter

from services.embeddings import get_embeddings, get_embeddings_large
from services.retrievers import retrieve_passages_cosine, retrieve_passages_ip, retrieve_passages_l2, \
    retrieve_passages_cosine_large, retrieve_passages_ip_large, retrieve_passages_l2_large

route = APIRouter(
    tags=["Passage Retrieval"]
)


@route.post("/retrieve_cosine/")
async def retrieve_cosine(query, k):
    query_vector = get_embeddings(query)
    response = retrieve_passages_cosine(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}


@route.post("/retrieve_cosine_large/")
async def retrieve_cosine(query, k):
    query_vector = get_embeddings_large(query)
    response = retrieve_passages_cosine_large(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}


@route.post("/retrieve_ip/")
async def retrieve_inner_product(query, k):
    query_vector = get_embeddings(query)
    response = retrieve_passages_ip(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}


@route.post("/retrieve_ip_large/")
async def retrieve_inner_product(query, k):
    query_vector = get_embeddings_large(query)
    response = retrieve_passages_ip_large(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}


@route.post("/retrieve_l2/")
async def retrieve_l2(query, k):
    query_vector = get_embeddings(query)
    response = retrieve_passages_l2(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}



@route.post("/retrieve_l2_large/")
async def retrieve_l2(query, k):
    query_vector = get_embeddings_large(query)
    response = retrieve_passages_l2_large(query_vector, k)
    passages = response.passages
    return {'message': 'Similar passages retrieved!', 'Passages': passages}
