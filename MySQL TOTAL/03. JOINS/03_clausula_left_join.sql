SELECT
	Series.titulo AS 'Título de la serie', 
	Episodios.titulo AS 'Título del episodio'
FROM Series
LEFT JOIN Episodios
ON Series.serie_id = Episodios.serie_id
ORDER BY Series.titulo;