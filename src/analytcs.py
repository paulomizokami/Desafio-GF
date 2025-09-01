# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

############################################################################################################
#### Análise ###############################################################################################
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

#Criando bases PBI
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