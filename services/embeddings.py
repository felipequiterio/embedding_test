import torch
from transformers import AutoTokenizer, AutoModel

from utils.log import get_custom_logger
from utils.time import log_time

logger = get_custom_logger('EMBEDDINGS')


@log_time('Loading tokenizer')
def load_tokenizer():
    return AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')


@log_time('Loading model')
def load_model():
    return AutoModel.from_pretrained('neuralmind/bert-base-portuguese-cased')


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
model = load_model()


def get_embeddings(text):
    logger.info(f'Starting to process text: "{text}"')
    input_ids = tokenize_text(tokenizer, text)
    cls_embedding = generate_embeddings(model, input_ids)
    logger.info(f'Embeddings dimension: {cls_embedding.size()}')
    embedding = cls_embedding.tolist()
    return embedding

