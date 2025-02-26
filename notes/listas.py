import os
os.system('cls' if os.name == 'nt' else 'clear')
from random import randint 


lista_numeros = [0, 2, 5]
print(lista_numeros[0])

lista_numeros[0] = 5
print(lista_numeros[0])

lista_numeros.append('Hello Word')
print(lista_numeros)


for c in range (1, 6):
    print(c)

numbers = []
for c in range(2):
    num_user = int(input('digite um numero: '))
    numbers.append(num_user)

print(sum(numbers))

sort_number = randint(1, 5)

validador = False
while not validador:
    number_user = int(input('Advinhe o numero sorteado: '))
    if number_user == sort_number:
        print('PARABENS, VOCE ACERTOU O NUMERO KKKK')
        validador = True
    elif number_user > sort_number:
        print('MENOS')
    elif number_user < sort_number:
        print('MAIS')







