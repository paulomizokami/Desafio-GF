# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Atribuindo arquivos as variaveis
client = pd.read_csv("data/clientes.csv", encoding="utf-8-sig")
sales = pd.read_csv("data/vendas.csv", encoding="utf-8-sig")
product = pd.read_csv("data/produtos.csv", encoding="utf-8-sig")

# Dicionário com correspondência UF → Estado
uf_para_estado = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

# Criar nova coluna com o nome do estado
client['nome_estado'] = client['estado'].map(uf_para_estado)

# Add coluna quantidade
sales['quantidade'] = 1
# Tratamento marca null Base de produtos
def update_marca(nome_produto):
    if 'NOTEBOOK' in nome_produto.upper():
        return 'Notebook'
    elif 'GELADEIRA' in nome_produto.upper():
        return 'Geladeira'
    elif 'FERRO DE PASSAR' in nome_produto.upper():
        return 'Ferro de Passar'
    elif 'IMPRESSORA' in nome_produto.upper():
        return 'Impressora'
    elif 'MONITOR' in nome_produto.upper():
        return 'Monitor'
    elif 'LUMIN' in nome_produto.upper():
        return 'Luminaria'
    elif 'REL' in nome_produto.upper():
        return 'Relogio de Parede'
    elif 'ESCOVA SECADORA' in nome_produto.upper():
        return 'Escova Secadora'
    elif 'BALAN' in nome_produto.upper():
        return 'Balanca'
    elif 'CADEIRA DE ESCRIT' in nome_produto.upper():
        return 'Cadeira de Escritorio'
    else:
        return 'Desconhecida'

product['marca'] = product.apply(
    lambda row: update_marca(row['nome_produto']) if pd.isnull(row['marca']) else row['marca'],
    axis=1
)
# Remove duplicidade
client.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)
product.drop_duplicates(inplace=True)

# Conversão de dados
sales['data_venda'] = pd.to_datetime(sales['data_venda'], errors='coerce')
sales['valor'] = sales['valor'].astype(float)

# Merge de Bases
BU = sales.merge(client, on="id_cliente", how="inner")
BU = BU.merge(product, on="id_produto", how="left")

# Tratamento nome_produto, descricao e marca null
BU[['nome_produto', 'descricao', 'marca']] = BU[['nome_produto', 'descricao', 'marca']].fillna('Desconhecido')

# Cria base Unificada
BU.to_csv('databasetoBI/base_unificada.csv', index=False, encoding="utf-8-sig")


########################################################################################
# Lendo a base
dadaanalytcs = pd.read_csv("databasetoBI/base_unificada.csv")
# Produtos mais vendido
top_produtos = dadaanalytcs.groupby('nome_produto')['quantidade'].sum().sort_values(ascending=False).head(10)

# Canais com melhor performance
vendas_canais = dadaanalytcs.groupby('canal_venda')['quantidade'].sum().sort_values(ascending=False)

dadaanalytcs['data_venda'] = pd.to_datetime(dadaanalytcs['data_venda'])
dadaanalytcs['ano_mes'] = dadaanalytcs['data_venda'].dt.to_period('M')

vendas_mes = dadaanalytcs.groupby('ano_mes')['quantidade'].sum()

#Criando bases PBI QTD
# Produto
# Transformando em DataFrame
top_produtos_df = top_produtos.reset_index()  # 'nome_produto' vira coluna
top_produtos_df.columns = ['nome_produto', 'quantidade_vendida']  # renomeando colunas

# Salvar em CSV
top_produtos_df.to_csv("databasetoBI/top_10_produtos.csv", index=False, encoding="utf-8-sig")

# Canais
# Transformando em DataFrame
vendas_canais_df = vendas_canais.reset_index()  # 'canal_venda' vira coluna
vendas_canais_df.columns = ['canal_venda', 'quantidade_vendida']  # renomeando colunas

# Salvar em CSV
vendas_canais_df.to_csv("databasetoBI/vendas_por_canal.csv", index=False, encoding="utf-8-sig")

# Sazonalidade
# Transformar em DataFrame
vendas_mes_df = vendas_mes.reset_index()
vendas_mes_df.columns = ['ano_mes', 'quantidade_vendida']

# Salvar em CSV
vendas_mes_df.to_csv("databasetoBI/vendas_por_mes.csv", index=False, encoding="utf-8-sig")

#Criando bases PBI Fat
# Produto

# Produtos maior faturamento
top_produtos = dadaanalytcs.groupby('nome_produto')['valor'].sum().sort_values(ascending=False).head(10)
# Transformando em DataFrame
top_produtos_df = top_produtos.reset_index()  # 'nome_produto' vira coluna
top_produtos_df.columns = ['nome_produto', 'Faturamento']  # renomeando colunas

# Salvar em CSV
top_produtos_df.to_csv("databasetoBI/top_10_produtos_fat.csv", index=False, encoding="utf-8-sig")


# Canais com melhor performance
vendas_canais = dadaanalytcs.groupby('canal_venda')['valor'].sum().sort_values(ascending=False)
# Canais
# Transformando em DataFrame
vendas_canais_df = vendas_canais.reset_index()  # 'canal_venda' vira coluna
vendas_canais_df.columns = ['canal_venda', 'Faturamento']  # renomeando colunas

# Salvar em CSV
vendas_canais_df.to_csv("databasetoBI/vendas_por_canal_fat.csv", index=False, encoding="utf-8-sig")

# Sazonalidade

dadaanalytcs['data_venda'] = pd.to_datetime(dadaanalytcs['data_venda'])
dadaanalytcs['ano_mes'] = dadaanalytcs['data_venda'].dt.to_period('M')

vendas_mes = dadaanalytcs.groupby('ano_mes')['valor'].sum()
# Transformar em DataFrame
vendas_mes_df = vendas_mes.reset_index()
vendas_mes_df.columns = ['ano_mes', 'Faturamento']

# Salvar em CSV
vendas_mes_df.to_csv("databasetoBI/vendas_por_mes_fat.csv", index=False, encoding="utf-8-sig")
