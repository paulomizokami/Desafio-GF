# Importando bibliotecas
import pandas as pd
import numpy as np

# Atribuindo arquivos as variaveis
client = pd.read_csv("data/clientes.csv")
sales = pd.read_csv("data/vendas.csv")
product = pd.read_csv("data/produtos.csv")

# Remove duplicidade
client.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)
product.drop_duplicates(inplace=True)

# Conversao de dados
sales['data_venda'] = pd.to_datetime(sales['data_venda'], errors='coerce')
client['id_cliente'] = pd.to_numeric(sales['id_cliente'], errors='coerce')
sales['id_cliente'] = pd.to_numeric(sales['id_cliente'], errors='coerce')

# Visualizar as 5 primeiras linhas de cada base
print("Clientes:")
print(client.head())

print("Vendas:")
print(sales.head())

print("Produtos:")
print(product.head())

# Verifica valores nulos
print("Valores nulos em Clientes:\n", client.isnull().sum())
print("Valores nulos em Vendas:\n", sales.isnull().sum())
print("Valores nulos em Produtos:\n", product.isnull().sum())

# Supondo que as chaves são: cliente_id e produto_id

sales_client = sales.merge(client, on="id_cliente", how="left")
sales_client.to_csv('basecliente.csv', index=False)
print("Base cliente exportada.csv")
#BU = sales_client.merge(product, on="id_produto", how="left")

# Verificando resultado
#print(BU.head())
#BU.to_csv
#BU.to_excel('base_tratada.xlsx', index=False)
#print("Base exportada como base_tratada.csv")



