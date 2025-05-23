# %%
import pandas as pd
from IPython.display import display
from sqlalchemy import create_engine

# %%
#lendo arquivo csv
df = pd.read_csv('relatorio.csv')
df.head()

# %%
# 2. **Transformação**

#    - Remova linhas com valores nulos em campos essenciais (`cliente`, `produto`, `valor`).


#    - Converta a coluna `valor` para numérico, tratando erros.
df['valor'] = pd.to_numeric(df_not_null['valor'], errors='coerce')
df_not_null = df.dropna()
display(df_not_null)




# %%
# 3. Cria nova coluna com imposto de 12%
df_not_null.loc[:, 'imposto'] = df_not_null['valor'] * 1.12
display(df_not_null)

# %%
#Carga

#Salve o resultado em um novo arquivo vendas_processadas.csv ou carregue os dados em um banco SQLite.

df_not_null.to_csv('relatorio_limpo.csv', sep=',')

# %%
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
banco = 'pipeline01'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{banco}')
tabela = 'relatorio_limpo'

#enviando ao banco de dados
df.to_sql(tabela, engine, if_exists='replace', index=False)
print("Dados inseridos com sucesso!")


