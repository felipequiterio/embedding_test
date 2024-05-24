import pandas as pd


def read_csv(file_path):
    df = pd.read_csv(file_path, encoding='windows-1252')
    return df['questions'].tolist()
