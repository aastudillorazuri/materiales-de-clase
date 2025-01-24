SELECT titulo, duracion FROM Episodios
ORDER BY duracion ASC; -- Se puede omitir el ASC y se obtiene el mismo resultado

SELECT titulo, duracion FROM Episodios
ORDER BY duracion DESC;

SELECT titulo, duracion FROM Episodios
ORDER BY titulo;

SELECT titulo, duracion FROM Episodios
ORDER BY titulo DESC;