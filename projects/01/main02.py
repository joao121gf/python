import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('ola')

inventory = {
    'product': ['Notebook', 'Tablet', 'Impressora', 'Cadeira'],
    'category': ['Eletronicos', 'Eletronicos', 'Escritório', 'Escritório'],
    'amount_sale': [50, 30, 20, 50],
    'unit_price': [3500, 1500, 800, 600],
    'sale_date': ['2025-02-01', '2025-02-05', '2025-02-08', '2025-02-10']
}

df_inventory = pd.DataFrame(inventory)

#Ver o total de vendas de cada produto e adcionar nova coluna total_sales
df_inventory['total_sales'] = df_inventory['amount_sale'] * df_inventory['unit_price']
# print(df_inventory)


#Agrupar por categoria e calcular o total de vendas por categoria.
p_category = df_inventory.groupby('category')['total_sales'].sum()
# print(p_category)


#Ordenar o DataFrame do maior para o menor valor total de vendas
orderer = df_inventory.sort_values(by='total_sales', ascending=False)
# print(orderer[['product', 'unit_price']])


#Filtrar produtos que venderam mais de 25 unidades.
more25 = df_inventory[df_inventory['amount_sale'] > 30] 
print(more25)