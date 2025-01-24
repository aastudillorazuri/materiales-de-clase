SELECT * FROM Series
WHERE genero = 'Ciencia ficción'
UNION ALL
SELECT * FROM Series
WHERE genero = 'Drama';

SELECT * FROM Series
WHERE genero = 'Ciencia ficción'
UNION ALL
SELECT * FROM Series
WHERE genero = 'Drama'
UNION ALL
SELECT * FROM Series
WHERE genero = 'Drama';