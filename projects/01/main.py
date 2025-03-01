import pandas as pd
import os
from random import randint, choice
from datetime import datetime, timedelta
os.system('cls' if os.name == 'nt' else 'clear')


#Creating data frame with informations about product, category, quantity sold, unite price, sale data and discount

categories = ['Gaming', 'Accessories', 'Accessories', 'Gaming', 'Gaming']
table = {
    'product': ['Smartphone', 'Mouse', 'Keyboard', 'Monitor', 'Processors'],
    'category': categories,
    'quantity_sold': [200, 150, 120, 80, 300],  
    'unit_price': [1500, 50, 100, 1200, 300],  
    'sale_date': [
        datetime(2025, 2, 1),  
        datetime(2025, 2, 3),
        datetime(2025, 2, 5),
        datetime(2025, 2, 7),
        datetime(2025, 2, 9)
    ],
    'discount': [0.05, 0.1, 0.15, 0.05, 0]  
}

df_table = pd.DataFrame(table)


#create new columns as TOTAL SALES ( unity price * quantity_sold) and PRICE WITH DISCOUNT 
print('\033[93mData Frame\033[0m')
df_table['total_sales'] = df_table['unit_price'] * df_table['quantity_sold']
df_table['price_discount'] = df_table['unit_price'] - (df_table['unit_price'] * df_table['discount'])
print(df_table)
print('\033[92m____________________________________________\033[0m')



#agroup the datas per category and calculate the total sales for each category
print('\033[93mEach categories and yours total sales: he media, max and min sales per category: \033[0m')
gaming_category = df_table.groupby('category')['total_sales'].sum()
print(gaming_category)
print('\033[92m____________________________________________\033[0m')

#calculate the media and the max sales por category
print('\033[93mThe media, max and min sales per category: \033[0m')
gaming_sumary = df_table.groupby('category')['total_sales'].agg(['mean', 'max', 'min'])
print(gaming_sumary)
print('\033[92m____________________________________________\033[0m')


#Perform agregation to see the best sales days
print('\033[93mThe best sales day: \033[0m')

best_performance_day = df_table.sort_values(by='total_sales', ascending=False)[['sale_date', 'total_sales']]
print(best_performance_day)
print('\033[92m____________________________________________\033[0m')


#Filter the datas for each products with price bigger than to 100 and calculate the total sales that products

print('\033[93mFiltering products with more than 100 sales from the highest number of sales to the lowest: \033[0m')

more_100 = df_table[df_table['quantity_sold'] >= 100]
orderer = more_100.sort_values(by='total_sales', ascending=False)
print(orderer)
print('\033[92m____________________________________________\033[0m')

