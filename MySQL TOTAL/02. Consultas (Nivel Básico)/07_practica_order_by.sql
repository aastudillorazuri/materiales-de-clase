/*
Escribe una consulta SQL que seleccione todos los años de lanzamiento únicos de la 
tabla Series.
Los resultados deben estar ordenados de forma descendente, es decir, del más reciente 
al más antiguo.
Ordenar por el campo año_lanzamiento de forma descendente (DESC).
Seleccionar únicamente valores de año_lanzamiento únicos.
*/

SELECT DISTINCT año_lanzamiento
FROM Series
ORDER BY año_lanzamiento DESC;

/*
Escribe una consulta SQL que seleccione los nombres (nombre) y las fechas de nacimiento 
(fecha_nacimiento) de todos los actores desde la tabla Actores.
Ordena los resultados de manera descendente (DESC) por la fecha de nacimiento, lo que 
significa que los actores más jóvenes aparecerán primero en tu lista.
*/

SELECT nombre, fecha_nacimiento
FROM Actores
ORDER BY fecha_nacimiento DESC;