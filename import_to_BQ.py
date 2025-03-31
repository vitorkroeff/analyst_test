# Pacotes Utilizados
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
from pandas_gbq import to_gbq
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Lista com os nomes dos arquivos CSV
# e os nomes das tabelas no BigQuery
bases_csv = [ 'BASES/Clientes.csv', 'BASES/Estoque.csv', 'BASES/Fornecedores.csv', 'BASES/Produtos.csv', 'BASES/Vendas.csv']
table_names_bq = ['clientes', 'estoque', 'fornecedores', 'produtos', 'vendas']

clientes = pd.read_csv('BASES/Clientes.csv', sep=';', encoding='latin1')


# função para importar os dados para o BigQuery
def load_to_bq(data_frame, dataset_id, table_id, project_id):
    try:
        # Define a referência da tabela
        table_ref = f"{dataset_id}.{table_id}"
        
        # Escreve o DataFrame no BigQuery
        to_gbq(
            data_frame,
            destination_table=table_ref,
            project_id=project_id,
            if_exists='append',  # Pode ser 'replace', 'append' ou 'fail'
        )
        print("Carga para o BigQuery concluída com sucesso.")

    except Exception as e:
        print(f"Erro ao carregar dados para o BigQuery: {e}")

# loop for para iterar sobre os arquivos CSV e as tabelas no BigQuery
for i in range(len(bases_csv)):
    # Lê o arquivo CSV
    data_frame = pd.read_csv(bases_csv[i], sep=';', encoding='latin1')
    
    # Define o dataset_id e table_id
    dataset_id = 'Bases Teste Analista de Dados'
    table_id = table_names_bq[i]
    
    # Define o project_id
    project_id = os.getenv('BQ_PROJECT_ID')
    
    # Chama a função para carregar os dados no BigQuery
    load_to_bq(data_frame, dataset_id, table_id, project_id)