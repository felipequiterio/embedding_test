
# Projeto de Teste de Embedding Retrieval com pgvector

Este projeto é um exemplo de como usar embeddings com pgvector para recuperar passagens relevantes de um banco de dados PostgreSQL. Ele inclui scripts para configuração do banco de dados, inserção de dados e execução de consultas de recuperação tanto via console quanto via API.

## Pré-requisitos

1. **WSL (Windows Subsystem for Linux)**
   - Siga as instruções de instalação da Microsoft:
     [Guia de Instalação do WSL](https://learn.microsoft.com/pt-br/windows/wsl/install)
   - Comando de instalação:
     ```sh
     wsl --install
     ```

2. **Docker**
   - Instale o Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Passos de Configuração

1. **Baixar a Imagem do Docker com Postgres e pgvector**
   - Execute o comando abaixo para baixar a imagem:
     ```sh
     docker pull ankane/pgvector
     ```

2. **Inicializar o Container com Variáveis de Ambiente**
   - Use o comando abaixo para iniciar o container com as variáveis de ambiente necessárias:
     ```sh
     docker run --name pgvector-container -e POSTGRES_DB=qa -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=vector -d ankane/pgvector
     ```

3. **Configuração do Banco de Dados**
   - Dentro do projeto, execute o script `setup.py` para configurar o banco de dados:
     ```sh
     python database/setup.py
     ```

4. **Inserir Dados no Banco de Dados**
   - Execute o script `add_data.py` para inserir os dados necessários. Este script só precisa ser executado uma vez:
     ```sh
     python add_data.py
     ```

## Executando o Projeto

### Via Console

- Para rodar o teste de recuperação de passagens via console, execute o script `test.py`:
  ```sh
  python test.py
  ```

### Via API

- Para rodar a API, execute o script `main.py` e acesse a documentação da API em [http://localhost:9000/docs#/](http://localhost:9000/docs#/):
  ```sh
  python main.py
  ```

## Customização da Função de Distância

- Se estiver usando via console e quiser alterar a função de distância usada, edite a linha 11 no arquivo `test.py` para usar qualquer outra função de distância disponível:
  ```python
  # Exemplo: Mudar para a função de distância L2
  retrieve_passages_l2()
  ```

## Estrutura do Projeto

```
embedding_test/
├── api/
│   └── routes/
│       ├── __init__.py
│       ├── embedding_route.py
│       └── retriever_route.py
├── data/
│   └── sample_docs/
│       └── question_dataset.csv
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── create.py
│   ├── insert.py
│   ├── setup.py
│   └── table.py
├── services/
│   ├── __init__.py
│   ├── embeddings.py
│   └── retrievers.py
├── utils/
│   ├── __init__.py
│   ├── log.py
│   ├── reader.py
│   └── time.py
├── add_data.py
├── assertion.log
├── azure_openai_usage.log
├── main.py
├── openai_usage.log
├── requirements.txt
├── server.py
└── test.py
```

## Dependências

- Certifique-se de instalar todas as dependências necessárias listadas no arquivo `requirements.txt`:
  ```sh
  pip install -r requirements.txt
  ```
