/*
Escribe una consulta SQL que genere una lista que muestre el título de cada 
serie junto con el título y duración de sus episodios.
Sin embargo, solo incluirás en tu resultado aquellos episodios que tengan una 
duración mayor a 30 minutos.
Ordena los resultados alfabéticamente por el título de la serie.
Los alias exactos que debes aplicar sobre las columnas son:
- Título de la Serie
- Título del Episodio
- Duración
*/

SELECT
    s.titulo AS 'Título de la Serie',
    e.titulo AS 'Título del Episodio',
    e.duracion AS 'Duración'
FROM Series s
RIGHT JOIN Episodios e
ON e.serie_id = s.serie_id
WHERE duracion > 30
ORDER BY s.titulo ASC;