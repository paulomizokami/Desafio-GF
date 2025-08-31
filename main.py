# Importar bibliotecas principais
import pandas as pd
import numpy as np

# Carregar os arquivos
clientes = pd.read_csv("C:/Users/AMD/Documents/Projeto_GF/arq/desafio_gerando_falcoes/GF/clientes.csv")
#vendas = pd.read_csv("data/vendas.csv")
#produtos = pd.read_csv("data/produtos.csv")

# Visualizar as 5 primeiras linhas de cada base
print("Clientes:")
print(clientes.head())
