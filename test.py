from services.embeddings import get_embeddings
from services.retrievers import retrieve_passages_cosine
from utils.log import get_custom_logger

logger = get_custom_logger('TEST')

embedding = get_embeddings('Explique o que é um algoritimo?')

response = retrieve_passages_cosine(embedding, 5)
print('Retrieved Questions:')
print('-' * 30)
for i, passage in enumerate(response.passages, start=1):
    print(f"Passage {i}: \n{passage['question']}\n")
    print('-' * 30)
