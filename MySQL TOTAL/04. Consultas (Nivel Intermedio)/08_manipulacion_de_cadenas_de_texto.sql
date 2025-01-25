SELECT UPPER(titulo) AS Titulo_Mayusculas
FROM Series;

SELECT LOWER(nombre) AS nombre_en_minusculas
FROM Actores;

SELECT CONCAT(titulo, ' (', año_lanzamiento, ')') AS Titulo_Año
FROM Series;

SELECT titulo, SUBSTRING(titulo, 1, 5) AS Extracto_Titulo
FROM Episodios;

SELECT SUBSTRING(titulo, 1, 5) AS Extracto_Titulo
FROM Episodios;

SELECT titulo, LENGTH(titulo) AS Longitud_Titulo
FROM Series;

SELECT
	titulo,
    LEFT(titulo, 3) AS Inicio_Titulo,
    RIGHT(titulo, 3) AS Fin_Titulo
FROM Series;