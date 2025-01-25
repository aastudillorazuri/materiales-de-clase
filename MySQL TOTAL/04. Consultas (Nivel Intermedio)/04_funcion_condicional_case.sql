SELECT
	titulo,
	año_lanzamiento,
    CASE
		WHEN año_lanzamiento >= 2020 THEN 'Nueva'
        WHEN año_lanzamiento BETWEEN 2010 AND 2019 THEN 'Clásica'
        -- WHEN año_lanzamiento >= 2010 AND año_lanzamiento >= 2019 THEN 'Clásica'
        ELSE 'Antigua'
	END AS categoria
FROM Series;