from database.insert import insert_data
from services.embeddings import get_embeddings, get_embeddings_large
from utils.reader import read_csv


def main():
    questions = read_csv('data/sample_docs/question_dataset.csv')

    data_to_insert = []
    for i, question in enumerate(questions):
        print(f'Adding data {i} of {len(questions)}')
        embedding = get_embeddings_large(question)
        data_to_insert.append((question, embedding))

    table_name = "text_vector_embeddings_large"
    columns = ["question", "embedding"]
    insert_data(table_name, columns, data_to_insert)

#main()
