import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')


sales_data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price': [3000, 150, 200, 1000],
    'quantity_sold': [10, 50, 20, 15]
}

data_frame = pd.DataFrame(sales_data)


# Calculando faturamento total (price * quantity_sold)
data_frame['total_revenue'] = data_frame['price'] * data_frame['quantity_sold']

# print(data_frame)
# print(data_frame.describe())

#Crie uma coluna chamada total_sales que multiplica prices por sold
restaurant = {
    'foods': ['Pizza', 'Burger', 'Pasta', 'Salad'],
    'category': ['Fast Food', 'Fast Food', 'Italian', 'Healthy'],
    'prices' : [30, 25, 40, 20],
    'sold': [100, 80, 50, 90]
}

df_restaurant = pd.DataFrame(restaurant)
df_restaurant['total_sales'] = df_restaurant['prices'] * df_restaurant['sold']




# Exercício 2 - Intermediário 🟡
# Com base no exercício 1:

# Filtre apenas os produtos com preço acima de 30
# Filtre apenas os produtos vendidos mais de 80 vezes
higher_30 = df_restaurant['foods'][df_restaurant['prices'] > 30]


more_80 = df_restaurant[df_restaurant['sold'] > 80]
# print(more_80)



# Exercício 3 - Avançado 🔴
# Calcule a média de preços
# Calcule a soma total das vendas (total_sales)
# Encontre o produto mais caro
average = df_restaurant['prices'].sum() / len(df_restaurant['prices'])
# print(average)

sum_total_sales = df_restaurant['sold'].sum()
# print(sum_total_sales)

expensive = max(df_restaurant['prices'])
# print(expensive)

sorted_prices = df_restaurant.sort_values(by='prices')
# print(sorted_prices)

sorted_prices_Desc = df_restaurant.sort_values(by='prices', ascending=False)

# print(sorted_prices_Desc)


# Ordenando por categoria e depois por preço de forma decrescente
sorted_data = df_restaurant.sort_values(by=['category', 'prices'], ascending=[True, False])
# print(sorted_data)



filtered_data = df_restaurant.query('prices > 30 and category== "Eletronics" ')
# print(filtered_data)


# Exercícios
# Ordenação simples: Ordene os restaurantes de acordo com o preço, do mais barato ao mais caro.
order = df_restaurant.sort_values(by=['prices'])
# print(order)



# Ordenação múltipla: Ordene os restaurantes pela categoria em ordem crescente e, dentro de cada categoria, ordene os preços de forma decrescente.
o_category = df_restaurant.sort_values(by=['category', 'prices'], ascending=[True, False])
# print(o_category)

# Filtragem avançada: Filtre todos os restaurantes com preços acima de 30 e com a categoria "Electronics".

filter_2 = df_restaurant.query('prices > 30 and category == "Italian" ')
print(filter_2)