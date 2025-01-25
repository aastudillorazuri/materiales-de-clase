SELECT * FROM Episodios
WHERE serie_id = 13; -- Esta opción no es la más eficiente

SELECT * FROM Episodios
WHERE serie_id = (
	SELECT serie_id FROM Series
    WHERE titulo = 'The Office'
    );

SELECT * FROM Episodios
WHERE serie_id = (
	SELECT serie_id FROM Series
    WHERE titulo = 'Sherlock'
    );