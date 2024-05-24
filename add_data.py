from database.insert import insert_data
from services.embeddings import get_embeddings
from utils.reader import read_csv


def main():
    questions = read_csv('data/sample_docs/teste.csv')

    data_to_insert = []
    for i, question in enumerate(questions):
        print(f'Adding data {i} of {len(questions)}')
        embedding = get_embeddings(question)
        data_to_insert.append((question, embedding))

    table_name = "text_vector_embeddings_testecsv"
    columns = ["question", "embedding"]
    insert_data(table_name, columns, data_to_insert)

main()
