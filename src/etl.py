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
print("Base exportada como base_unificada.csv")