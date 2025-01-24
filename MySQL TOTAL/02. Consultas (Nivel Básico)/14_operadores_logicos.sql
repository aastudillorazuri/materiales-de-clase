SELECT titulo, duracion, rating_imdb
FROM Episodios
WHERE duracion > 45;

SELECT titulo, duracion, rating_imdb
FROM Episodios
WHERE duracion > 45 AND rating_imdb >= 9;

SELECT * FROM Series
WHERE genero = 'Comedia';

SELECT * FROM Series
WHERE genero = 'Comedia' OR genero = 'Animación'; -- WHERE (genero = 'Comedia' OR genero = 'Animación')

SELECT * FROM Series
WHERE genero <> 'Comedia';