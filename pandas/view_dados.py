#Visualização de Dados com Pandas
# O Pandas permite criar gráficos rapidamente através da integração com Matplotlib e Seaborn.

#pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')


inventory = {
    'product': ['Notebook', 'Tablet', 'Impressora', 'Cadeira'],
    'category': ['Eletronicos', 'Eletronicos', 'Escritório', 'Escritório'],
    'amount_sale': [50, 30, 20, 50],
    'unit_price': [3500, 1500, 800, 600],
    'sale_date': ['2025-02-01', '2025-02-05', '2025-02-08', '2025-02-10']
}


df_inventory = pd.DataFrame(inventory)
df_inventory['total_sales'] = df_inventory['amount_sale'] * df_inventory['unit_price']


# media_price = df_inventory.groupby('category')['unit_price'].agg(['mean'])
# media_price.plot(kind='bar', color='blue')
# plt.title('Titulo')
# plt.ylabel('y')
# plt.xlabel('x')
# #plt.show()


plt.scatter(df_inventory['unit_price'], df_inventory['amount_sale'], color='blue')
plt.grid(True)
plt.title('teste')
plt.ylabel('amout_sale')
plt.xlabel('unit_price')
plt.show()





# ##GRAFICO DE BARRA
# df_inventory.plot(x='product', y='total_sales', kind='bar', color='blue')
# plt.title('Total de vendas por produto') #titulo da tabela
# plt.ylabel('Total de vendas') #titulo esquerda y
# plt.xlabel('produto') #nome dos produtos em baixo




# ##GRAFICO DE LINHA
# # Ótimo para visualizar mudanças ao longo do tempo.

# df_inventory.plot(x='sale_date', y='total_sales', kind='line', marker='o', color='green')
# plt.title('titulo')
# plt.ylabel('total vendas')
# plt.xlabel('data')
# plt.grid(True)
# # plt.show()


# marker='o' adciona pontos aos valores
# grid=true adciona uma grade para facilitar a vizualizacao




# GRAFICO DE PIZZA
# Bom para visualizar proporções entre categorias

# df_inventory.groupby('category')['total_sales'].sum().plot(kind='pie', autopct='%1.1f%%')
# plt.title('Distribuição de Vendas por Categoria')
# plt.ylabel('')
# # plt.show()

# .groupby('category')['total_sales'].sum(): Agrupa as vendas por categoria.
# kind='pie': Define o tipo de gráfico como pizza.
# autopct='%1.1f%%': Adiciona os valores percentuais.


