from typing import Union, List, Optional

import dspy
import psycopg2
import psycopg2.extras

from fastapi import FastAPI

from database.connection import connect_database
from utils.log import get_custom_logger

app = FastAPI()
logger = get_custom_logger('RETRIEVER')


def retrieve_passages_cosine(query_or_queries: Union[str, List[str]], k: Optional[int] = None):
    conn = connect_database()
    if not conn:
        return dspy.Prediction(passages=[])

    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logger.info('Retrieving passages with cosine distance')
        sql_query = """
            SELECT question
            FROM text_vector_embeddings
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
        """
        cur.execute(sql_query, (query_or_queries, k))
        results = cur.fetchall()
        passages = [{'question': result['question']} for result in
                    results]
        cur.close()
        logger.info('Passages retrieved.')
        return dspy.Prediction(passages=passages)
    except psycopg2.Error as e:
        logger.error(f"Failed to retrieve data: {e}")
        return dspy.Prediction(passages=[])
    finally:
        if conn:
            conn.close()


def retrieve_passages_l2(query_or_queries: Union[str, List[str]], k: Optional[int] = None):
    conn = connect_database()
    if not conn:
        return dspy.Prediction(passages=[])

    try:
        logger.info('Retrieving passages with L2 distance')

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        sql_query = """
            SELECT question
            FROM text_vector_embeddings
            ORDER BY embedding <-> %s::vector
            LIMIT %s;
        """
        cur.execute(sql_query, (query_or_queries, k))
        results = cur.fetchall()
        passages = [{'question': result['question']} for result in
                    results]
        cur.close()
        logger.info('Passages retrieved.')

        return dspy.Prediction(passages=passages)
    except psycopg2.Error as e:
        logger.error(f"Failed to retrieve data: {e}")
        return dspy.Prediction(passages=[])
    finally:
        if conn:
            conn.close()


def retrieve_passages_ip(query_or_queries: Union[str, List[str]], k: Optional[int] = None):
    conn = connect_database()
    if not conn:
        return dspy.Prediction(passages=[])

    try:
        logger.info('Retrieving passages with inner product distance')

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        sql_query = """
            SELECT question
            FROM text_vector_embeddings
            ORDER BY embedding <#> %s::vector
            LIMIT %s;
        """
        cur.execute(sql_query, (query_or_queries, k))
        results = cur.fetchall()
        passages = [{'question': result['question']} for result in
                    results]
        cur.close()
        logger.info('Passages retrieved.')
        return dspy.Prediction(passages=passages)
    except psycopg2.Error as e:
        logger.error(f"Failed to retrieve data: {e}")
        return dspy.Prediction(passages=[])
    finally:
        if conn:
            conn.close()