SELECT fecha_estreno, YEAR(fecha_estreno), MONTH(fecha_estreno)
FROM Episodios;

SELECT fecha_estreno, DATE_ADD(fecha_estreno, INTERVAL 30 DAY)
FROM Episodios;

SELECT fecha_estreno, DATE_ADD(fecha_estreno, INTERVAL -30 DAY)
FROM Episodios;

SELECT 
	*,
	DATEDIFF(CURDATE(), fecha_estreno) AS diasdesdeestreno
FROM Episodios;