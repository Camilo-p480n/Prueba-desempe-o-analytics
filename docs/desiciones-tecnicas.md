# Decisiones tecnicas

Algunas cosas que hice de cierta forma y por que.

## Clientes sinteticos con seed fija
Use la API de randomuser.me con seed='emausoft' para que los 100 clientes
sean siempre los mismos cada vez que se corra el pipeline. Sin seed cada
ejecucion genera gente diferente y eso rompe cualquier analisis comparativo.

## Asignacion de clientes a ordenes
El dataset de ventas no tiene un campo de cliente, asi que tuve que inventar
uno. Lo hice asignando clientes aleatoriamente a cada orden con semilla fija
(seed=42).Una alternativa mas realista hubiera sido asignar por pais, pero requeria que los paises de clientes coincidieran con los de ventas y eso no pasaba.

## Cache para la API de paises
La primera vez que corre fetch_paises.py descarga todo de restcountries.com
y lo guarda en data/interim/paises.csv. Las siguientes veces lee directo
del archivo. para disminuir tiempos de carga 

## Nombres de paises inconsistentes
El dataset usa USA y UK, restcountries devuelve United States y United Kingdom con un diccionario manual de dos entradas

## Estructura (COOKIECOTTER)
segun lo que investigue esta es una estructura muy utilizada en la ciencia de datos, ya que esta estandarizada y es consistente, flexible, tambien nos ahorra tiempo a la hora de programar debido a estas caracteristicas