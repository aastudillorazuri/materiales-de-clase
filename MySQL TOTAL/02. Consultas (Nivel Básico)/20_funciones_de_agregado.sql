SELECT SUM(duracion) FROM Episodios;

SELECT SUM(duracion) AS suma_duracion FROM Episodios;

SELECT SUM(duracion) AS suma_duracion FROM Episodios
WHERE serie_id = 5;

SELECT COUNT(*) FROM Episodios;

SELECT COUNT(*) FROM Episodios
WHERE serie_id = 2;

SELECT * FROM Episodios
WHERE serie_id = 2;

SELECT MAX(duracion) FROM Episodios
WHERE serie_id = 2;

SELECT MIN(duracion) FROM Episodios
WHERE serie_id = 2;

SELECT AVG(duracion) FROM Episodios;

SELECT AVG(duracion) FROM Episodios
WHERE serie_id IN (1, 2);