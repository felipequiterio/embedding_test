import psycopg2

from database.connection import connect_database


def insert_data(table_name, columns, data):

    try:
        conn = connect_database()
        cur = conn.cursor()

        columns_formatted = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {table_name} ({columns_formatted}) VALUES ({placeholders});"
        cur.executemany(query, data)
        conn.commit()
        print(f"Data inserted successfully into {table_name}.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error inserting data into {table_name}: ", error)
    finally:
        if not conn.closed:
            conn.close()