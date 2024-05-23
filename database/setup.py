from database.create import create_text_vector_table
from database.table import list_tables, describe_table, fetch_and_print_data

create_text_vector_table()

list_tables()

describe_table('text_vector_embeddings')

# truncate_table('text_vector_embeddings')

# fetch_and_print_data('text_vector_embeddings')
