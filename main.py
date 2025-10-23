import subprocess # A biblioteca para "chamar" outros scripts
import sys        # A biblioteca para acessar o sistema

print("--- Iniciando Pipeline de ETL Completo ---")

# 1. Definimos a ordem dos scripts que queremos rodar
lista_scripts = [
    'scripts/coleta_api.py',
    'scripts/limpeza_transformacao.py',
    'scripts/carga_sql.py'
]

# 2. Pegamos o caminho exato para o 'python.exe' que está rodando ESTE script
#    (Isso garante que vamos usar o 'python.exe' da nossa VENV)
python_exe = sys.executable

# 3. Criamos um loop para rodar cada script
for script in lista_scripts:
    print(f"\n--- Executando script: {script} ---")
    
    try:
        # 4. Usamos o 'subprocess.run' para rodar o comando:
        resultado = subprocess.run(
            [python_exe, script],
            check=True, # Se o script falhar (der erro), o Python vai parar aqui.
            capture_output=True, # Pega o que o script 'printou'.
            text=True, # Formata o 'print' como texto.
            encoding='utf-8' # Boa prática para acentuação
        )
        
        # 5. Se deu certo, mostramos os 'prints' do script
        print("--- Saída do Script (stdout): ---")
        print(resultado.stdout)
        
    except subprocess.CalledProcessError as e:
        # 6. Se 'check=True' falhou, o script deu erro!
        print(f"\n*** ERRO AO EXECUTAR O SCRIPT: {script} ***")
        print("--- O pipeline foi INTERROMPIDO. ---")
        
        # Mostra o erro exato que o script deu
        print("--- Erro (stderr): ---")
        print(e.stderr)
        
        # Para o 'main.py' imediatamente
        break
    except FileNotFoundError:
        # 7. (Erro extra) Se o script não foi encontrado
        print(f"\n*** ERRO: Arquivo não encontrado: {script} ***")
        print("--- O pipeline foi INTERROMPIDO. ---")
        break

else:
    # 8. O 'else' do 'for' loop:
    #    Só roda se o 'for' loop completou SEM 'break' (ou seja, sem erros)
    print("\n--- SUCESSO! Pipeline de ETL concluído. ---")
    print("--- Todos os scripts foram executados. ---")
    print("--- O banco de dados 'indicadores_database.db' está atualizado. ---")