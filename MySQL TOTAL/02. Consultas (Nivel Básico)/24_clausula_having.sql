SELECT serie_id, COUNT(episodio_id) AS numero_episodios
FROM Episodios
GROUP BY serie_id
HAVING COUNT(episodio_id) > 10;

SELECT serie_id, COUNT(episodio_id) AS numero_episodios
FROM Episodios
GROUP BY serie_id
HAVING COUNT(episodio_id) > 11;

SELECT serie_id, COUNT(episodio_id) AS numero_episodios
FROM Episodios
WHERE serie_id IN (2, 12)
GROUP BY serie_id
HAVING COUNT(episodio_id) > 11;