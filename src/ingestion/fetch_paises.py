import requests, pandas as pd
from pathlib import Path

#URL y parámetros para obtener datos de países desde restcountries.com
URL    = 'https://restcountries.com/v3.1/all'
FIELDS = 'name,cca2,cca3,region,subregion,latlng'
ROOT   = Path(__file__).resolve().parents[2]

#
MAPEO_PAISES = {
    'USA': 'United States',
    'UK':  'United Kingdom',
}

#función para obtener los datos de países desde la API, con caching en un archivo CSV local
def fetch_paises():
    cache = ROOT / 'data/interim/paises.csv'
    if cache.exists():
        print(f'Leyendo desde cache: {cache}')
        return pd.read_csv(cache)
    resp = requests.get(URL, params={'fields': FIELDS}, timeout=60)
    resp.raise_for_status()
    df = normalizar(resp.json())
    cache.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache, index=False)
    return df


#Función para normalizar los datos obtenidos y convertirlos en un DataFrame
def normalizar(raw):
    filas = []
    for c in raw:
        filas.append({
            'pais':      c['name']['common'],
            'iso2':      c.get('cca2'),
            'iso3':      c.get('cca3'),
            'region':    c.get('region'),
            'subregion': c.get('subregion'),
            'lat':       c.get('latlng',[None,None])[0],
            'lng':       c.get('latlng',[None,None])[1],
        })
    return pd.DataFrame(filas)


#
def enriquecer_ventas(df_ventas, df_paises):
    df = df_ventas.copy()
    df['pais_norm'] = df['COUNTRY'].replace(MAPEO_PAISES)
    df_merged = df.merge(df_paises, left_on='pais_norm',
                         right_on='pais', how='left')
    sin_match = df_merged[df_merged['region'].isnull()]['COUNTRY'].unique()
    if len(sin_match) > 0:
        print(f'Paises sin match: {sin_match}')
    else:
        print('Todos los paises encontraron match')
    return df_merged


#Ejecuta la función de enriquecimiento y guarda el resultado en un nuevo archivo CSV
if __name__ == '__main__':
    df_paises  = fetch_paises()
    print(f'Paises: {len(df_paises)}')
    ventas = ROOT / 'data/interim/ventas_con_cliente.csv'
    if ventas.exists():
        df_v = pd.read_csv(ventas)
        df_e = enriquecer_ventas(df_v, df_paises)
        df_e.to_csv(ROOT / 'data/interim/ventas_enriquecida.csv', index=False)