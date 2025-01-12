# Importamos Pandas
import pandas as pd

# Creamos una serie de números y hallamos su media
numeros = pd.Series([1, 2, 3, 5, 67, 35, 235, 62])
print(numeros.mean())

# Hallamos la suma de dichos números
print(numeros.sum())

# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['rojo', 'amarillo', 'verde'])

# Visualizamos la serie creada
print(colores)

# Creamos una serie con tipos de autos, y la visualizamos
tipos_autos = pd.Series(['Sedán', 'SUV', 'Pick-up'])
print(tipos_autos)

# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({'Tipo de auto': tipos_autos, 'Color': colores})
print(tabla_autos)