import psycopg2
from utils.log import get_custom_logger

logger = get_custom_logger('DATABASE')


def connect_database():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        logger.info('Connecting to database...')
        conn = psycopg2.connect(
            dbname="qa",
            user="admin",
            password="vector",
            host="localhost",
            port="5500"
        )
        logger.info("Database connected!")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)


def disconnect_database(conn):
    """ Disconnect from the PostgreSQL database server """
    try:
        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
