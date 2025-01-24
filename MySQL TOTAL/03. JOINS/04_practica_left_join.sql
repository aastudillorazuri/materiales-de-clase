/*
Escribe una consulta SQL que devuelva, para cada serie, su título, el título 
de cada episodio asociado (si hay alguno), y el rating de IMDb.
Los alias exactos que debes aplicar son: Título de la Serie, Título del 
Episodio, Rating IMDB.
Ordena los resultados por el título de la serie de forma ascendente.
*/

SELECT 
    s.titulo AS 'Título de la Serie', 
    e.titulo AS 'Título del Episodio', 
    e.rating_imdb AS 'Rating IMDB' 
FROM Series s
LEFT JOIN Episodios e
ON s.serie_id = e.serie_id
ORDER BY s.titulo ASC;

/*
Escribe una consulta SQL que muestre el título de la serie, el título de 
cada episodio, y el rating de IMDb para todos los episodios de la serie 
'Stranger Things'.
Ordena los resultados por Episodios.rating_imdb de forma descendente (de 
mayor a menor) según rating de imdb.
Los alias exactos que debes aplicar sobre las columnas son: Título de la 
Serie, Título del Episodio, Rating IMDB.
*/

SELECT
    s.titulo AS 'Título de la Serie', 
    e.titulo AS 'Título del Episodio', 
    e.rating_imdb AS 'Rating IMDB'
FROM Series s
LEFT JOIN Episodios e
ON s.serie_id = e.serie_id
WHERE s.titulo = 'Stranger Things'
ORDER BY e.rating_imdb DESC;