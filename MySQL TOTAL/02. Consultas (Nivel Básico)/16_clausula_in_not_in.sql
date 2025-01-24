SELECT * FROM Series
WHERE genero NOT IN ('Comedia');

SELECT * FROM Series
WHERE genero IN ('Comedia');

SELECT * FROM Series
WHERE genero IN ('Comedia', 'Fantasía');

SELECT * FROM Series
WHERE genero NOT IN ('Comedia', 'Fantasía');