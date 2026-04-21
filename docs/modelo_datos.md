# Modelo de datos — Emausoft Analytics

## Tipo de modelo
Esquema estrella (Star Schema)

## Diagrama

```
                 dim_fecha
                     |
dim_clientes --- fact_ventas --- dim_geografia
                     |
               dim_productos
```

## Tablas

### fact_ventas (tabla de hechos)
| Columna          | Tipo    | Descripcion                        |
|------------------|---------|------------------------------------|
| order_number     | int     | Identificador de la orden          |
| producto_id      | int     | Clave foranea a dim_productos      |
| cliente_id       | int     | Clave foranea a dim_clientes       |
| fecha_id         | int     | Clave foranea a dim_fecha          |
| geografia_id     | int     | Clave foranea a dim_geografia      |
| quantity_ordered | int     | Cantidad de productos ordenados    |
| price_each       | decimal | Precio unitario                    |
| sales            | decimal | Venta total de la linea            |
| status           | string  | Estado de la orden                 |

### dim_productos
| Columna         | Tipo    | Descripcion            |
|-----------------|---------|------------------------|
| producto_id     | int     | Clave primaria         |
| producto_nombre | string  | Codigo del producto    |
| categoria       | string  | Linea de producto      |
| precio_lista    | decimal | Precio de lista (MSRP) |

### dim_clientes
| Columna    | Tipo   | Descripcion        |
|------------|--------|--------------------|
| cliente_id | int    | Clave primaria     |
| nombre     | string | Nombre completo    |
| ciudad     | string | Ciudad del cliente |
| pais       | string | Pais del cliente   |
| email      | string | Email del cliente  |
| genero     | string | Genero del cliente |

### dim_geografia
| Columna      | Tipo   | Descripcion              |
|--------------|--------|--------------------------|
| geografia_id | int    | Clave primaria           |
| pais         | string | Nombre del pais          |
| iso2         | string | Codigo ISO 2 letras      |
| iso3         | string | Codigo ISO 3 letras      |
| region       | string | Continente               |
| subregion    | string | Subregion geografica     |
| lat          | float  | Latitud del centroide    |
| lng          | float  | Longitud del centroide   |

### dim_fecha
| Columna    | Tipo   | Descripcion               |
|------------|--------|---------------------------|
| fecha_id   | int    | Clave primaria (YYYYMMDD) |
| fecha      | date   | Fecha completa            |
| ano        | int    | Ano                       |
| mes        | int    | Mes (1-12)                |
| trimestre  | int    | Trimestre (1-4)           |
| dia        | int    | Dia del mes               |
| dia_semana | string | Nombre del dia            |

## Relaciones
| Desde       | Hacia                      | Cardinalidad |
|-------------|----------------------------|--------------|
| fact_ventas | dim_productos.producto_id  | N:1          |
| fact_ventas | dim_clientes.cliente_id    | N:1          |
| fact_ventas | dim_fecha.fecha_id         | N:1          |
| fact_ventas | dim_geografia.geografia_id | N:1          |

