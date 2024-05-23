import torch
from transformers import AutoTokenizer, AutoModel

from utils.log import get_custom_logger
from utils.time import log_time

logger = get_custom_logger('EMBEDDINGS')


@log_time('Loading tokenizer')
def load_tokenizer():
    return AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')


@log_time('Loading tokenizer large')
def load_tokenizer_large():
    return AutoTokenizer.from_pretrained('neuralmind/bert-large-portuguese-cased')


@log_time('Loading model')
def load_model():
    return AutoModel.from_pretrained('neuralmind/bert-base-portuguese-cased')


@log_time('Loading model')
def load_model_large():
    return AutoModel.from_pretrained('neuralmind/bert-large-portuguese-cased')


@log_time('Tokenizing text')
def tokenize_text(tokenizer, text):
    return tokenizer.encode(text, return_tensors='pt')


@log_time('Generating embeddings')
def generate_embeddings(model, input_ids):
    logger.info('Generating embeddings.')
    with torch.no_grad():
        outs = model(input_ids)
        hidden_states = outs.last_hidden_state
        cls_embedding = hidden_states[0, 0]  # Using [CLS] token embedding
    return cls_embedding


tokenizer = load_tokenizer()
#tokenizer_large = load_tokenizer_large()

model = load_model()
#model_large = load_model_large()


def get_embeddings(text):
    logger.info(f'Starting to process text: "{text}"')
    input_ids = tokenize_text(tokenizer, text)
    cls_embedding = generate_embeddings(model, input_ids)
    logger.info(f'Embeddings dimension: {cls_embedding.size()}')
    embedding = cls_embedding.tolist()
    return embedding

#
# def get_embeddings_large(text):
#     logger.info(f'Starting to process text: "{text}"')
#     input_ids = tokenize_text(tokenizer_large, text)
#     cls_embedding = generate_embeddings(model_large, input_ids)
#     logger.info(f'Embeddings dimension: {cls_embedding.size()}')
#     embedding = cls_embedding.tolist()
#     return embedding
