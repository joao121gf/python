import os
os.system('cls' if os.name == 'nt' else 'clear')


tickets = 50
buyers = 250
have_enought_tickets = (tickets >= buyers)
if have_enought_tickets == True:
    print('Have tickets')
else :
    print('Havent tickets')


name = "Dev Python"
age = 24
weight = 72.3


print(f"Hi {name}, I know you are {age} years old and {weight} weight")

name2 = input("Type your name: ")
age2 = int(input('Type your age: '))
weight2 = float(input('Type your weight: '))
print(f'Hello {name2} welcome, i know you are {age2} years old and {weight2} weight')
print(type(age2))


soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30/3
potencia = 7**2

print(f'Soma {soma}')
print(f'Multi {multiplicacao}')
print(f'divisao {divisao}')
print(f'potencia {potencia}')


idade = int(input('Informe sua idade'))
if idade <=17:
    print('voce é menor de idade, entrada restrida')
else:
    print ('pode entrar')


