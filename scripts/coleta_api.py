import requests
import pandas as pd
from datetime import datetime

#Definindo indicadores para coleta
indicadores = {
    'IPCA': 433,
    'SELIC': 432,
    'PIB': 24369
}
#Definindo datas de coleta
data_inicio = "01/01/2017"
data_fim = datetime.now().strftime("%d/%m/%Y")


print("\n--- Definindo a função da coleta de dados ---\n")

#Função para coletar da API do BC
def coleta_dados(codigo_indicador, data_inicio_func, data_fim_func):
    url_api = f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_indicador}/dados?formato=json&dataInicial={data_inicio_func}&dataFinal={data_fim_func}"

    resposta = requests.get(url_api)
    if resposta.status_code == 200: # Status 200 significa sucesso
        dados_json = resposta.json()
        return dados_json
    else:
        print(f"ERRO! O servidor respondeu com falha. Status : {resposta.status_code}")
        return None


print("\n--- Executando a coleta ---\n")

#Lista em branco para ser alimentada
listadf = []

#Loop para criar dataframe com as listas
for nome_indicador, codigo_indicador in indicadores.items(): #Utiliza items por conta de coletar do dicionário indicadores ((Key : Value))
    dados_coletados = coleta_dados(codigo_indicador, data_inicio, data_fim)

    if dados_coletados:
        df = pd.DataFrame(dados_coletados)
        df.insert(0, 'nome_indicador', nome_indicador)
        listadf.append(df)

        print(f"  > Sucesso ao coletar e tratar: {nome_indicador}")

    else:
        print(f"  > Falha ao obter dados do {nome_indicador}.")

#Juntar todos dataframes de indicadores em uma só tabela
df_final = pd.concat(listadf, ignore_index=True)

#Exportar tabela para um arquivo.csv
df_final.to_csv('dados/indicadores_brutos.csv', index=False)

print("\n--- Script 'coleta_api.py' concluído com sucesso! ---")
print("\n--- Um arquivo 'indicadores_brutos.csv' foi criado na pasta /dados ---\n")
