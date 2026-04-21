import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

#Construye el dataframe de productos a partir del dataframe de ventas
def build_productos(df_ventas):
    cols = ['PRODUCTCODE', 'PRODUCTLINE', 'MSRP']
    df = (df_ventas[cols]
          .drop_duplicates(subset=['PRODUCTCODE'])
          #reordena
          .reset_index(drop=True))
    df.insert(0, 'producto_id', range(1, len(df) + 1))
    df = df.rename(columns={
        'PRODUCTCODE': 'producto_nombre',
        'PRODUCTLINE': 'categoria',
        'MSRP':        'precio_lista',
    })
    return df

#Propaga el producto_id a las ventas uniendo con el dataframe de productos
def propagar_producto_id(df_ventas, df_productos):
    df = df_ventas.merge(
        df_productos[['producto_id', 'producto_nombre']],
        left_on='PRODUCTCODE', right_on='producto_nombre', how='left')
    df = df.drop(columns=['PRODUCTCODE', 'producto_nombre'])
    return df


#Ejecuta la función de construcción de productos y guarda el resultado en un nuevo archivo CSV, junto con las ventas enriquecidas con producto_id
if __name__ == '__main__':
    df_v = pd.read_csv(ROOT / 'data/raw/sales_data_sample.csv', encoding='latin-1')
    df_p = build_productos(df_v)
    print(f'Productos unicos: {len(df_p)}')
    df_p.to_csv(ROOT / 'data/interim/productos.csv', index=False)
    df_v2 = propagar_producto_id(df_v, df_p)
    df_v2.to_csv(ROOT / 'data/interim/ventas_con_producto.csv', index=False)
    print('Guardado: productos.csv y ventas_con_producto.csv')