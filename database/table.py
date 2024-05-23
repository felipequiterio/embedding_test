import psycopg2

from database.connection import connect_database
from utils.log import get_custom_logger

logger = get_custom_logger('DATABASE')


def list_tables():
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cur.fetchall()
        logger.info("Tables in the database:")
        for table in tables:
            logger.info(table[0])
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error listing tables: ", error)
    finally:
        if not conn.closed:
            conn.close()


def describe_table(table_name):
    try:
        conn = connect_database()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = %s;
        """, (table_name,))
        columns = cur.fetchall()
        if columns:
            logger.info(f"Schema of table '{table_name}':")
            for column in columns:
                logger.info(f"Column Name: {column[0]}, Data Type: {column[1]}")
        else:
            logger.warn(f"No columns found for table '{table_name}'.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error retrieving table schema: ", error)
    finally:
        if not conn.closed:
            conn.close()


def fetch_and_print_data(table_name):
    conn = connect_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name};")
            rows = cur.fetchall()
            print('-------------------- DATABASE -----------------------')
            print(f"Data from {table_name}:")
            for row in rows:
                print(row)
            print('------------------------------------------------------')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: ", error)
        finally:
            conn.close()


def truncate_table(table_name):
    try:
        conn = connect_database()
        cur = conn.cursor()

        query = f"TRUNCATE TABLE {table_name};"
        cur.execute(query)
        conn.commit()
        print(f"Table {table_name} truncated successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error truncating table {table_name}: ", error)
    finally:
        if conn and not conn.closed:
            conn.close()

# fetch_and_print_data('text_vector_embeddings')
# describe_table('text_vector_embeddings')
