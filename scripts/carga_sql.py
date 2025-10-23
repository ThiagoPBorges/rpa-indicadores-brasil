import pandas as pd
from sqlalchemy import create_engine

caminho_entrada = 'dados/indicadores_tratados.xlsx'

df = pd.read_excel(caminho_entrada, sheet_name='indicadores')

# Defina o nome do arquivo do banco de dados
caminho_banco = 'dados/indicadores_database.db'


print(f"\n--- Conectando ao banco de dados: {caminho_banco} ---")

# Defina o nome da tabela que vamos criar lá dentro
nome_tabela = 'indicadores'

# Crie o "motor" (a conexão) com o banco SQLite
engine = create_engine(f'sqlite:///{caminho_banco}')

print(f"--- Carregando dados na tabela '{nome_tabela}' ---")

df.to_sql(
    name=nome_tabela, #Nome da tabela no SQL
    con=engine, #Conexão com o banco
    if_exists='replace', #Se a tabela já existir, apague e crie de novo.
    index=False #Não salve o índice (0,1,2...) do pandas
)

