SELECT titulo, personaje 
FROM Series
JOIN Actuaciones -- INNER JOIN Actuaciones
ON Series.serie_id = Actuaciones.serie_id;

SELECT Series.titulo, Actuaciones.personaje 
FROM Series
INNER JOIN Actuaciones
ON Series.serie_id = Actuaciones.serie_id;

SELECT s.titulo, a.personaje 
FROM Series AS s
INNER JOIN Actuaciones AS a
ON s.serie_id = a.serie_id;

SELECT s.titulo, a.personaje 
FROM Series AS s
INNER JOIN Actuaciones AS a
ON s.serie_id = a.serie_id
WHERE titulo = 'The Crown'; -- WHERE s.titulo = 'The Crown'

SELECT s.titulo, a.personaje 
FROM Series AS s
INNER JOIN Actuaciones AS a
ON s.serie_id = a.serie_id
WHERE s.serie_id = 1; -- Se define en qué tabla se desea aplicar el filtro