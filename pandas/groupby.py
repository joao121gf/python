import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')


restaurant = {
    'foods': ['Pizza', 'Burger', 'Pasta', 'Salad'],
    'category': ['Fast Food', 'Fast Food', 'Italian', 'Healthy'],
    'prices' : [30, 25, 40, 20],
    'sold': [100, 80, 50, 90]
}

data_frame = pd.DataFrame(restaurant)
# print(data_frame)

category  = data_frame.groupby('category')['prices'].mean()
# print(category)


category_stats = data_frame.groupby('category')['prices'].agg(['mean', 'max', 'min'])
# print(category_stats)




# Exercícios
# Média dos preços por categoria: Calcule a média dos preços para cada categoria de restaurante.

media = data_frame.groupby('category')['prices'].mean()
# print(media)


# Operações múltiplas de agregação: Calcule o preço médio, máximo e mínimo de cada categoria usando agg().
media_total = data_frame.groupby('category')['prices'].agg(['mean', 'max', 'min'])
# print(media_total)

# Ajuste de preços: Aumente todos os preços de restaurantes da categoria "Electronics" em 15%.

data_frame.loc[data_frame['category'] == 'Italian', 'prices'] *= 1.15


print(data_frame)