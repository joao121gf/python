import pandas as pd
clientes = {
    'id': [1, 2, 3, 4],
    'nomes': ['Joao', 'Pedro', 'Robert', 'Stenis'],
    'idade': [20, 30, 40, 20],
    'cidade': ['sbo', 'bragança', 'sbo', 'turquia']   ,
    'compras': [2000, 500000, 2123, 2103023]
}

df = pd.DataFrame(clientes)
df.to_csv('clientes.csv', index=False)
print('Confimaro')