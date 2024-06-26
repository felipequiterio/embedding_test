import psycopg2

from database.connection import disconnect_database, connect_database
from utils.log import get_custom_logger

logger = get_custom_logger('TABLE')


def create_text_vector_table():
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""
                CREATE EXTENSION IF NOT EXISTS vector;
                """)
        logger.info('Extension created.')
        conn.commit()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS text_vector_embeddings (
                id SERIAL PRIMARY KEY,
                question TEXT,
                embedding vector(768)
            );
        """)
        conn.commit()
        logger.info("Table 'text_vector_embeddings' created successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error creating table: ", error)
    finally:
        disconnect_database(conn)


def create_text_vector_table_large():
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""
                CREATE EXTENSION IF NOT EXISTS vector;
                """)
        logger.info('Extension created.')
        conn.commit()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS text_vector_embeddings_large (
                id SERIAL PRIMARY KEY,
                question TEXT,
                embedding vector(1024)
            );
        """)
        conn.commit()
        logger.info("Table 'text_vector_embeddings_large' created successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error creating table: ", error)
    finally:
        disconnect_database(conn)


def create_text_vector_table_testecsv():
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""
                CREATE EXTENSION IF NOT EXISTS vector;
                """)
        logger.info('Extension created.')
        conn.commit()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS text_vector_embeddings_testecsv (
                id SERIAL PRIMARY KEY,
                question TEXT,
                embedding vector(768)
            );
        """)
        conn.commit()
        logger.info("Table 'text_vector_embeddings' created successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error creating table: ", error)
    finally:
        disconnect_database(conn)

def create_extension():
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""
        CREATE EXTENSION IF NOT EXISTS vector;
        """)
        conn.commit()
        logger.info('Extension created.')

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error creating table: ", error)
    finally:
        disconnect_database(conn)
