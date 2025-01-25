DESCRIBE Episodios;

SELECT * FROM Episodios
WHERE CAST(fecha_estreno AS DATE) >= '2010-01-01';

SELECT * FROM Episodios
WHERE CAST(fecha_estreno AS UNSIGNED) >= '2010-01-01'; -- No funciona correctamente