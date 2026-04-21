import pandas as pd
from pathlib import Path


#llama a al csv y lo carga en un dataframe
RAW = Path('data/raw/sales_data_sample.csv')
df = pd.read_csv(RAW, encoding='latin-1')

#imprime la info del dataframe
print(f'Shape: {df.shape}')
print(df.dtypes)
df.info()

#imprime cmpos nulos
print('\nNulos:')
print(df.isnull().sum().sort_values(ascending=False))


#imprime duplicados
print(f'Duplicados: {df.duplicated().sum()}')

#imprime el rango de fechas
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format='mixed')
print(f'Desde: {df["ORDERDATE"].min().date()}')
print(f'Hasta: {df["ORDERDATE"].max().date()}')

#imprime los paises y su cantidad de registros
print('\nPaises:')
print(df['COUNTRY'].value_counts())