SELECT serie_id, AVG(duracion) AS promedio, SUM(duracion) AS suma_duracion
FROM Episodios
WHERE serie_id IN (1, 2)
GROUP BY serie_id;

SELECT serie_id FROM Episodios
GROUP BY serie_id;

SELECT serie_id, COUNT(episodio_id) AS count_episodios
FROM Episodios
GROUP BY serie_id; -- GROUP BY 1 (hace referencia a la primera columna que exista en el SELECT)

SELECT serie_id, MAX(duracion) FROM Episodios
GROUP BY 1;