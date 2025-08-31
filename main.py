# Importar bibliotecas principais
import pandas as pd
import numpy as np

# Carregar os arquivos
client = pd.read_csv("data/clientes.csv")
sales = pd.read_csv("data/vendas.csv")
product = pd.read_csv("data/produtos.csv")

# Visualizar as 5 primeiras linhas de cada base
print("Clientes:")
print(client.head())

print("Vendas:")
print(sales.head())

print("Produtos:")
print(product.head())

