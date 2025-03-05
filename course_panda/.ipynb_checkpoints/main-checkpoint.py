import pandas as pd

url = 'course_panda/2004-2021.tsv'
df = pd.read_csv(url, sep='\t')
print(df.columns)
print(df['ESTADO'].head())