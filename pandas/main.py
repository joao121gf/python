import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')




# CRIANDO SERIES E DATA FRAMES
data = [10, 20, 30, 40, 50]
serie = pd.Series(data) # == cria uma serie com 4 numeros



people = ['Joao', 'Felix,', 'Renato']
age = [24, 32, 18]
serie2 = pd.Series(age, index=people)



cities = ['São Paulo', 'Pernambuco', 'Ceará', 'Piauí', 'Bahia']
populations = [44_000_000, 9_000_000, 9_200_000, 3_300_000, 14_900_000]
serie3 = pd.Series(populations, index=cities)


big_cities = serie3[serie3 > 10_000_000 ]
# print(big_cities)

serie3['Pernambuco'] = 9_100_000
# print(serie3)


#Exercice 1
fruits = ['Potato', 'Banana', 'Apple', 'Strawberry', 'Orange']
prices = [5.90, 2.50, 5.30, 12.90, 2.99]
colection = pd.Series(prices, index=fruits)




#Exercice 2
countries = ['Brasil', 'EUA', 'Canada', 'South Africa', 'Angola']
pib = [400_000_000, 900_000_000, 780_000_000, 290_000_000, 150_000_000]
colection_pib = pd.Series(pib, index=countries)
pib_colection_higher = colection_pib[colection_pib > 300_000_000]



#Exercice 3 
#Create a series with 5 students and your notes. after that modified the student specific note and return the notes media
students = ['Joao', 'Felix,', 'Renato', 'Pedro', 'Marcio']
notes = [10, 4, 5, 9, 8]
notes_serie = pd.Series(notes, index=students)



notes_serie['Pedro'] = 2



media_notes = sum(notes_serie.iloc) / len(notes)



notes_serie[notes_serie > 5] += 2



data = {
    'Nome': ['João', 'Felix', 'Renato', 'Pedro', 'Marcio'],
    'Nota': [10, 4, 5, 9, 8],
    'Idade': [16, 17, 16, 18, 17]
}


data_frame = pd.DataFrame(data) # criando um dataframe







km2 = [4000, 5000, 20000, 50000, 800000]
geoloca = {
    'Name': ['Santa barbara', 'Americana', 'Nova Odessa'],
    'Populations': [200_000, 300_000, 10_000],
    'area': [300, 500, 600]
}

employees = {
    'name': ['Pedro', 'Joao'],
    'age': [20, 31],
    'wage': [1500, 1800]
}
data_employ = pd.DataFrame(employees)
data_geo = pd.DataFrame(geoloca)

# print(data_employ[data_employ['age'] > 25])


products = {
    'name': ['glasses', 'glouves', 'computer', 'smartphone'],
    'category': ['Utensilies', 'Party', 'Eletronics', 'Eletronics'],
    'price': [200, 500, 5000, 2000]
}

data_products = pd.DataFrame(products)
filter_products = data_products[(data_products['category'] == 'Eletronics') & (data_products['price'] > 3000)]
print(filter_products)