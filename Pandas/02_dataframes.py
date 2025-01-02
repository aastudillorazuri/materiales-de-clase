'''
DataFrames

Un DataFrame es una estructura de datos bidimensional en Pandas, esencialmente una tabla con filas y columnas. Cada
columna de un DataFrame puede ser de un tipo diferente, similar a una hoja de cálculo, una tabla SQL o un diccionario
de Series. Los DataFrames son la estructura de datos principal en Pandas para manejar y analizar datos estructurados. 

Son útiles para representar datos reales en un formato tabular, permitiendo el análisis de grandes conjuntos de datos.
'''

import pandas as pd

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Madrid': [10, 12, 15, 17],
    'Barcelona': [12, 14, 16, 18],
    'Valencia': [14, 16, 18, 20],
    'Bilbao': [8, 10, 12, 14]
}

df_clima = pd.DataFrame(datos) # Contiene las temperaturas promedio (grados Celsius) de cuatro ciudades españolas para los primeros cuatro meses del año.

print(df_clima)