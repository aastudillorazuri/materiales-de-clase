SELECT * FROM Series
WHERE genero = 'Ciencia ficción'
UNION
SELECT * FROM Series
WHERE genero = 'Drama'
UNION
SELECT * FROM Series
WHERE genero = 'Drama';

SELECT titulo, genero FROM Series
WHERE genero = 'Ciencia ficción'
UNION
SELECT titulo, genero FROM Series
WHERE genero = 'Drama'
UNION
SELECT titulo, genero FROM Series
WHERE genero = 'Drama';