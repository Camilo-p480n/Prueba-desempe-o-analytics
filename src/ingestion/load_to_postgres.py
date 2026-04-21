import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()

HOST     = os.getenv('DB_HOST')
PORT     = os.getenv('DB_PORT')
NAME     = os.getenv('DB_NAME')
USER     = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

ENGINE = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}')

ROOT      = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / 'data/processed'

def cargar(df, nombre):
    df.to_sql(nombre, ENGINE, if_exists='replace', index=False)
    print(f'✅ {nombre}: {len(df)} filas cargadas')

if __name__ == '__main__':
    print(f'Conectando a {HOST}:{PORT}/{NAME}...\n')

    cargar(pd.read_csv(PROCESSED / 'fact_ventas.csv'),   'fact_ventas')
    cargar(pd.read_csv(PROCESSED / 'dim_clientes.csv'),  'dim_clientes')
    cargar(pd.read_csv(PROCESSED / 'dim_productos.csv'), 'dim_productos')
    cargar(pd.read_csv(PROCESSED / 'dim_geografia.csv'), 'dim_geografia')
    cargar(pd.read_csv(PROCESSED / 'dim_fecha.csv'),     'dim_fecha')

    print('\n✅ Todas las tablas cargadas correctamente')