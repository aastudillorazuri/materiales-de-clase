/*
Escribe una consulta SQL que seleccione todos los campos de las tablas Series y 
Episodios donde el serie_id coincida entre ambas tablas, utiliza un INNER JOIN 
para realizar el join entre ambas tablas.
*/

SELECT * FROM Series s
JOIN Episodios e
ON s.serie_id = e.serie_id;

/*
Escribe una consulta SQL que te permita obtener el título de la serie, el título 
de cada episodio y su duración de la serie 'Stranger Things'.
El resultado final debe contar con los siguientes nombres de columnas: 
titulo_serie, titulo_episodio, duracion.
*/

SELECT
    s.titulo AS titulo_serie,
    e.titulo AS titulo_episodio,
    e.duracion 
FROM Series s
JOIN Episodios e
ON s.serie_id = e.serie_id
WHERE s.titulo = 'Stranger Things';