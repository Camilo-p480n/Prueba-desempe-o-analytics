# Emausoft Analytics

Pipeline de datos y dashboard de ventas construido como prueba de desempeno.

## Descripcion
Proyecto de analisis de datos que integra un dataset de ventas con APIs
externas para construir un modelo estrella y visualizarlo en Power BI.

## Tecnologias
- Python 3.x — lenguaje principal del pipeline
- pandas, numpy — procesamiento de datos
- matplotlib, seaborn — visualizaciones en notebooks
- PostgreSQL — base de datos relacional
- DBeaver — cliente SQL y modelado
- Power BI Desktop — dashboard
- Git + GitHub — control de versiones

## Estructura del proyecto
```
emausoft-analytics/
├── data/
│   ├── raw/                      # Datos crudos, nunca se modifican
│   ├── interim/                  # Datos en procesamiento intermedio
│   └── processed/                # Datos limpios, listos para consumo
├── notebooks/
│   ├── 01_eda_ventas.ipynb
│   ├── 02_eda_clientes_api.ipynb
│   ├── 03_eda_regiones_api.ipynb
│   ├── 04_integracion.ipynb
│   └── 05_integracion.ipynb
├── src/
│   ├── ingestion/
│   │   ├── fetch_clientes.py     # Consume API randomuser.me
│   │   ├── fetch_paises.py       # Consume API restcountries.com
│   │   └── load_to_postgres.py   # Carga tablas en PostgreSQL
│   ├── cleaning/
│   │   ├── eda_ventas.py         # Analisis exploratorio de ventas
│   │   └── clean_ventas.py       # Limpieza del dataset
│   ├── transformation/
│   │   └── build_productos.py    # Construye dimension de productos
│   └── utils.py
├── dashboard/
│   └── emausoft.pbix
├── docs/
│   ├── modelo_datos.md
│   ├── decisiones.md
│   └── diagrama.png
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Requisitos previos
- Python 3.x con "Add Python to PATH" marcado
- PostgreSQL corriendo en localhost o servidor remoto
- DBeaver instalado
- Power BI Desktop instalado

## Instalacion
```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/emausoft-analytics.git
cd emausoft-analytics

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Variables de entorno
Crea un archivo .env en la raiz con:
```
DB_HOST=tu_host
DB_PORT=5432
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_password
```

## Orden de ejecucion del pipeline

```bash
# 1. EDA de ventas (solo consola)
python src/cleaning/eda_ventas.py

# 2. Consumir API de clientes
python src/ingestion/fetch_clientes.py

# 3. Consumir API de paises
python src/ingestion/fetch_paises.py

# 4. Limpiar ventas
python src/cleaning/clean_ventas.py

# 5. Construir tabla de productos
python src/transformation/build_productos.py

# 6. Correr notebooks en orden (jupyter notebook)
#    02_eda_clientes_api.ipynb  -> genera ventas_con_cliente.csv
#    03_eda_regiones_api.ipynb  -> genera ventas_enriquecida.csv
#    04_integracion.ipynb       -> genera ventas_con_producto.csv
#    05_integracion.ipynb       -> genera data/processed/ (5 archivos)

# 7. Cargar en PostgreSQL
python src/ingestion/load_to_postgres.py
```

## Archivos generados

| Archivo | Carpeta | Generado por |
|---|---|---|
| clientes.csv | data/interim/ | fetch_clientes.py |
| paises.csv | data/interim/ | fetch_paises.py |
| ventas_limpio.csv | data/interim/ | clean_ventas.py |
| ventas_con_cliente.csv | data/interim/ | Notebook 02 |
| ventas_enriquecida.csv | data/interim/ | Notebook 03 |
| productos.csv | data/interim/ | build_productos.py |
| ventas_con_producto.csv | data/interim/ | build_productos.py |
| fact_ventas.csv | data/processed/ | Notebook 05 |
| dim_clientes.csv | data/processed/ | Notebook 05 |
| dim_productos.csv | data/processed/ | Notebook 05 |
| dim_geografia.csv | data/processed/ | Notebook 05 |
| dim_fecha.csv | data/processed/ | Notebook 05 |

## Modelo de datos
Ver [docs/modelo_datos.md](docs/modelo_datos.md) para el detalle completo.

Esquema estrella con 1 tabla de hechos y 4 dimensiones:
- **fact_ventas** — metricas de ventas
- **dim_clientes** — atributos de clientes
- **dim_productos** — atributos de productos
- **dim_geografia** — pais, region, subregion
- **dim_fecha** — ano, mes, trimestre, dia

## Decisiones tecnicas
Ver [docs/decisiones.md](docs/decisiones.md) para el detalle completo.