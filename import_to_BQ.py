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

# Lê as bases de dados no formarto CSV





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