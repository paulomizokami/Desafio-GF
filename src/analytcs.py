# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

############################################################################################################
#### Análise por Quantidade ################################################################################
############################################################################################################

# Lendo a base
dadaanalytcs = pd.read_csv("databasetoBI/base_unificada.csv")
# Produtos mais vendido
top_produtos = dadaanalytcs.groupby('nome_produto')['quantidade'].sum().sort_values(ascending=False).head(10)

#Plot
plt.figure(figsize=(12,6))
sns.barplot(x=top_produtos.values, y=top_produtos.index, palette="viridis")
plt.title("Top 10 Produtos Mais Vendidos")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.show()

# Canais com melhor performance
vendas_canais = dadaanalytcs.groupby('canal_venda')['quantidade'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=vendas_canais.index, y=vendas_canais.values, palette='coolwarm')
plt.title("Vendas por Canal")
plt.ylabel("Quantidade Vendida")
plt.xlabel("Canal de Venda")
plt.show()

# Sazonalidade

dadaanalytcs['data_venda'] = pd.to_datetime(dadaanalytcs['data_venda'])
dadaanalytcs['ano_mes'] = dadaanalytcs['data_venda'].dt.to_period('M')

vendas_mes = dadaanalytcs.groupby('ano_mes')['quantidade'].sum()

vendas_mes.plot(kind='line', figsize=(12,6), marker='o')
plt.title("Vendas ao Longo do Tempo")
plt.xlabel("Ano-Mês")
plt.ylabel("Quantidade Vendida")
plt.grid()
plt.show()

############################################################################################################
#### Análise por Faturamento ###############################################################################
############################################################################################################

# Produtos maior faturamento
top_produtos = dadaanalytcs.groupby('nome_produto')['valor'].sum().sort_values(ascending=False).head(10)

#Plot
plt.figure(figsize=(12,6))
sns.barplot(x=top_produtos.values, y=top_produtos.index, palette="viridis")
plt.title("Top 10 Produtos Maior Faturamento")
plt.xlabel("Valor Faturamento")
plt.ylabel("Produto")
plt.show()

# Canais com melhor performance
vendas_canais = dadaanalytcs.groupby('canal_venda')['valor'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=vendas_canais.index, y=vendas_canais.values, palette='coolwarm')
plt.title("Faturamento por Canal")
plt.ylabel("Valor Faturamento")
plt.xlabel("Canal de Venda")
plt.show()

# Sazonalidade

dadaanalytcs['data_venda'] = pd.to_datetime(dadaanalytcs['data_venda'])
dadaanalytcs['ano_mes'] = dadaanalytcs['data_venda'].dt.to_period('M')

vendas_mes = dadaanalytcs.groupby('ano_mes')['valor'].sum()

vendas_mes.plot(kind='line', figsize=(12,6), marker='o')
plt.title("Faturamento ao Longo do Tempo")
plt.xlabel("Ano-Mês")
plt.ylabel("valor")
plt.grid()
plt.show()