import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

print(pd.__version__)


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

print(colection)
print(f"The Orange's price is {colection['Orange']}")


#Exercice 2
countries = ['Brasil', 'EUA', 'Canada', 'South Africa', 'Angola']
pib = [400_000_000, 900_000_000, 780_000_000, 290_000_000, 150_000_000]
colection_pib = pd.Series(pib, index=countries)
pib_colection_higher = colection_pib[colection_pib > 300_000_000]
print(pib_colection_higher.index[0])


#Exercice 3 
#Create a series with 5 students and your notes. after that modified the student specific note and return the notes media
students = ['Joao', 'Felix,', 'Renato', 'Pedro', 'Marcio']
notes = [10, 4, 5, 9, 8]
notes_serie = pd.Series(notes, index=students)


print(notes_serie)
notes_serie['Pedro'] = 2
print(notes_serie.iloc[0])


media_notes = sum(notes_serie.iloc) / len(notes)
print(media_notes)