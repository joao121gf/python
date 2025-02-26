import os
os.system('cls' if os.name == 'nt' else 'clear')

print('funciona')


alunos = {
    'Joaquin': 6
}

alunos = [
    {'nome': 'Joaquim', 'nota': 2},
    {'nome': 'Pirlo', 'nota': 8},
    {'nome': 'Anelka', 'nota': 6},
    {'nome': 'Henry', 'nota': 1},
    {'nome': 'Roberto Carlos', 'nota': 3},
    {'nome': 'Kaka', 'nota': 5},
    {'nome': 'Zinedini Zidani', 'nota': 3},
    {'nome': 'Joao', 'nota': 4},



]

# print(alunos[0]['nome'])


for c in alunos:
    print(f" {c['nome']}, nota: {c['nota']}")


# new_note = input('Escolha o usuario: ')
while True:
    nome_aluno = input('Digite o nome do aluno: ')
    aluno_encontrado = False
    for c in alunos:
        if c['nome'] == nome_aluno: # se o aluno for encontrado
           aluno_encontrado = True
           nova_nota = int(input('Digite a nova nota do aluno: '))
           c['nota'] = nova_nota
           break
    if aluno_encontrado:
        break
    else:
        print('ALUNO NAO ENCONTRADO. TENTE NOVAMENTE.')      
for c in alunos:
    print(f" {c['nome']}, nota: {c['nota']}")
    




        
