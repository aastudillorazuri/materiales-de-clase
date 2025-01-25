/*
Escribe una consulta SQL que seleccione el titulo de todas las series de la tabla 
Series junto con una nueva columna denominada 'Antigüedad'.
Esta columna debe mostrar 'Antigua' para las series lanzadas antes del año 2010 y 
'Reciente' para las series lanzadas en 2010 o después, puedes utilizar el campo 
año_lanzamiento para realizar dicha clasificación.
*/

SELECT
    titulo,
    CASE
        WHEN año_lanzamiento < 2010 THEN 'Antigua'
        ELSE 'Reciente'
    END AS 'Antigüedad'
FROM Series;

/*
Escribe una consulta SQL que seleccione el titulo de todas las series y una nueva 
columna llamada 'Categoría de Género'.
Esta columna debe reflejar si el género de la serie es 'Drama' o 'Comedia', 
clasificándolas como 'Dramático' o 'Divertido', respectivamente.
Para cualquier otro género, la clasificación debe ser 'Otro'.
Usa la sentencia CASE para asignar estas categorías.
*/

SELECT
    titulo,
    CASE
        WHEN genero = 'Drama' THEN 'Dramático'
        WHEN genero = 'Comedia' THEN 'Divertido'
        ELSE 'Otro'
    END AS 'Categoría de Género'
FROM Series;