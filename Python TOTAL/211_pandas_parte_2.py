# Importamos Pandas
import pandas as pd

# Importar "211_ventas_autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv(r'C:\Users\USER\Documents\Data\materiales-de-clase\Python TOTAL\211_ventas_autos.csv')
print(ventas_autos)

# Exportar el Dataframe como un archivo CSV a una carpeta local
ventas_autos.to_csv(r'C:\Users\USER\Documents\Data\materiales-de-clase\Python TOTAL\211_ventas_autos_final.csv')

# Analicemos los tipos de datos disponibles en el dataset de ventas autos
print(ventas_autos.dtypes)

# Apliquemos estadística descriptiva al dataset
print(ventas_autos.describe())

# Obtenemos información del dataset utilizando info()
print(ventas_autos.info())

# Listamos los nombres de las columnas de nuestro dataset
print(ventas_autos.columns)

# Averiguamos el "largo" de nuestro dataset
print(len(ventas_autos))

# Mostramos las primeras 5 filas del dataset
print(ventas_autos.head())

# Mostramos las primeras 7 filas del dataset
print(ventas_autos.head(7))

# Mostramos las últimas 5 filas del dataset
print(ventas_autos.tail())

# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
print(ventas_autos.loc[3])

# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
print(ventas_autos.iloc[[3, 7, 9]])

# Seleccionar la columna "Kilometraje"
print(ventas_autos['Kilometraje'])

# Encontrar el valor medio de la columnas "Kilometraje"
print(ventas_autos['Kilometraje'].mean())

# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
print(ventas_autos[ventas_autos['Kilometraje'] > 100000])

# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
print(pd.crosstab(ventas_autos['Fabricante'], ventas_autos['Puertas']))

# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
print(ventas_autos.groupby(['Fabricante']).mean(numeric_only=True))