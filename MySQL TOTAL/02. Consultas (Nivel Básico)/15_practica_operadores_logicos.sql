/*
Escribe una consulta SQL que seleccione todas las columnas de todas las series 
en la tabla Series, donde el género sea 'Drama' o 'Ciencia ficción'.
*/

SELECT * FROM Series
WHERE genero = 'Drama' OR genero = 'Ciencia ficción';