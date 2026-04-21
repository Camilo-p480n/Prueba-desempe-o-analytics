import requests, pandas as pd, numpy as np
from pathlib import Path

#URL y parámetros para obtener datos de clientes ficticios desde randomuser.me
URL    = 'https://randomuser.me/api/'
PARAMS = {'results': 100, 'seed': 'emausoft'}
ROOT   = Path(__file__).resolve().parents[2]

#Función para obtener los datos de clientes desde la API
def fetch_clientes():
    resp = requests.get(URL, params=PARAMS, timeout=30)
    resp.raise_for_status()
    return resp.json()['results']


#Función para normalizar los datos obtenidos y convertirlos en un DataFrame
def normalizar(raw_users):
    filas = []
    for u in raw_users:
        filas.append({
            'nombre': f"{u['name']['first']} {u['name']['last']}",
            'ciudad': u['location']['city'],
            'pais':   u['location']['country'],
            'email':  u['email'],
            'genero': u['gender'],
        })
    df = pd.DataFrame(filas)
    
    #Agrega una columna de ID de cliente con valores únicos
    df.insert(0, 'cliente_id', range(1, len(df) + 1))
    return df


#Función para asignar clientes a las ventas de forma aleatoria
def asignar_clientes(df_ventas, df_clientes):
    #genera un número aleatorio para cada orden y lo asigna a un cliente_id existente
    rng = np.random.default_rng(seed=42)
    #Obtiene los números de orden únicos y asigna un cliente_id aleatorio a cada uno
    ordenes = df_ventas['ORDERNUMBER'].unique()
    #Crea un diccionario de asignación donde cada número de orden se asigna a un cliente_id aleatorio
    asignacion = {o: rng.integers(1, len(df_clientes)+1) for o in ordenes}
    #Agrega la columna cliente_id al dataframe de ventas utilizando el diccionario de asignación
    df_ventas = df_ventas.copy()
    #Mapea cada número de orden a su cliente_id correspondiente y lo asigna a la nueva columna cliente_id
    df_ventas['cliente_id'] = df_ventas['ORDERNUMBER'].map(asignacion)
    return df_ventas


#crea el dataframe de clientes y lo guarda en un archivo CSV
if __name__ == '__main__':
    raw = fetch_clientes()
    df  = normalizar(raw)
    out = ROOT / 'data/interim/clientes.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f'Guardado: {out}')