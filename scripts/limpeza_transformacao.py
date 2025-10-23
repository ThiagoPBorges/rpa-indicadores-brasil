import pandas as pd

#Lê o arquivo csv criado pelo script de coleta
df = pd.read_csv('dados/indicadores_brutos.csv')

#Transformação a coluna de data em type date
df['data'] = pd.to_datetime(df['data'], format = '%d/%m/%Y')

#Criação colunas novas
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['mes_ano'] = df['data'].dt.to_period('M').astype(str)
df['trimestre'] = df['data'].dt.to_period('Q').astype(str)

#Salvando o dataframe tratado em csv
df.to_excel('dados/indicadores_tratados.xlsx', index=False, sheet_name='indicadores')

print(df.head())
print(df.info())