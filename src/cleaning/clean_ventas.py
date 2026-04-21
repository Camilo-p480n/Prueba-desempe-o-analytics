import pandas as pd
from pathlib import Path

#Define la ruta raíz del proyecto ruta relativa al archivo actual
ROOT = Path(__file__).resolve().parents[2]


#Función para limpiar el dataframe de ventas
def clean_ventas(df):
    df = df.copy()
    
    #Convierte la columna de fecha a datetime, limpia espacios y mayúsculas en columnas de texto, elimina duplicados y estandariza nombres de columnas
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format='mixed')
    str_cols = df.select_dtypes(include=['object', 'str']).columns
    for col in str_cols:
        df[col] = df[col].str.strip().str.upper()
    antes = len(df)
    df = df.drop_duplicates()
    print(f'Duplicados eliminados: {antes - len(df)}')
    df.columns = [c.lower() for c in df.columns]
    return df

#Ejecuta la función de limpieza y guarda el resultado en un nuevo archivo CSV
if __name__ == '__main__':
    df = pd.read_csv(ROOT / 'data/raw/sales_data_sample.csv', encoding='latin-1')
    df_limpio = clean_ventas(df)
    out = ROOT / 'data/interim/ventas_limpio.csv'
    df_limpio.to_csv(out, index=False)
    print(f'Guardado: {out}')
