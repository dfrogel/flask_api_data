import zipfile
import pandas as pd
import os

zip_path = r'script_python\dados (2).zip'

# Função para extrair arquivos zip
def descompactar_arquivo(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('.')

# Função para processar os dados
def processar_arquivos():
    descompactar_arquivo(zip_path)

    dados = pd.read_csv('origem-dados.csv')
    tipos = pd.read_csv('tipos.csv')

    # Adicionar a coluna nome_tipo no dataframe dados
    dados = dados.merge(tipos, left_on='tipo', right_on='id', how='left')

    # Remover a coluna id
    dados = dados.rename(columns={'nome': 'nome_tipo'}).drop(columns=['id'])

    # Filtrar arquivos com STATUS como CRITICO
    dados_criticos = dados[dados['status'] == 'CRITICO']

    # Ordenar os dados pelo campo CREATED_AT de forma decrescente
    dados_criticos = dados_criticos.sort_values(by='created_at', ascending=False)

    # Gerar arquivo sql
    gerar_sql(dados_criticos)

    print("\nArquivos extraidos com sucesso!")

    os.remove('origem-dados.csv')
    os.remove('tipos.csv')

    print("\nArquivos removidos com sucesso!")

# Função para gerar o arquivo sql
def gerar_sql(dados, lotes = 10 ):
    sql_path = os.path.join(os.path.dirname(__file__), 'insert-dados.sql')
    with open(sql_path, 'w') as f:
        for i in range(0, len(dados), lotes):
            dados_lote = dados[i:i+lotes]
            f.write(f"--Lote {i//lotes +1}\n")
            f.write(f"INSERT INTO dados_finais (created_at, product_code, customer_code, status, tipo, nome_tipo) VALUES \n")

            values = []
            for _, row in dados_lote.iterrows():
                linha = f"('{row['created_at']}', {row['product_code']}, {row['customer_code']}, '{row['status']}', {row['tipo']}, '{row['nome_tipo']}')"
                values.append(linha)

            f.write(",\n".join(values) + ";\n")
    
        # Query diária de agrupamento de tipos
        query = """
        SELECT 
            DATE(created_at) AS data,
            nome_tipo,
            COUNT(*) AS quantidade
        FROM
            dados_finais
        GROUP BY
            data, nome_tipo;
        """
        f.write(query)

    print("\nArquivo insert-dados.sql gerado com sucesso!")

# Chamando a função
processar_arquivos()
