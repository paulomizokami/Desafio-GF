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

# Produtos mais vendidos
top_produtos = dadaanalytcs.groupby('nome_produto')['quantidade'].sum().sort_values(ascending=False).head(10)

# Transformando em DataFrame
top_produtos_df = top_produtos.reset_index()  # 'nome_produto' vira coluna
top_produtos_df.columns = ['nome_produto', 'quantidade_vendida']  # renomeando colunas

# Salvar em CSV
top_produtos_df.to_csv("top_10_produtos.csv", index=False)

# Plot
plt.figure(figsize=(12,6))
sns.barplot(x='quantidade_vendida', y='nome_produto', data=top_produtos_df, palette="viridis")
plt.title("Top 10 Produtos Mais Vendidos")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.show()