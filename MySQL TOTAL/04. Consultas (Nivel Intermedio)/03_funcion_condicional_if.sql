SELECT
	titulo,
	rating_imdb,
    IF(rating_imdb > 8, 'Alto', 'Bajo') AS 'Categoría de Rating'
FROM Episodios;

SELECT
	nombre,
	YEAR(fecha_nacimiento) AS año_nacimiento,
    IF(YEAR(fecha_nacimiento) > 2000, 'Young', 'Old') AS 'Categoría de actores'
FROM Actores;