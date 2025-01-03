'''
Lectura de datos

Es el primer paso en cualquier flujo de trabajo de análisis de datos. Pandas proporciona una serie de funciones para cargar
datos desde varios formatos de archivo directamente en un DataFrame. La función pd.read_csv() es probablemente una de las más
utilizadas debido a la popularidad del formato CSV (Valores Separados por Comas) para el intercambio de datos.
'''

import pandas as pd

####################################################### Ejemplo 1 #######################################################
# Ruta al archivo CSV
archivo_temperaturas = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_temperaturas_globales.csv'

# Leer CSV 'temperaturas_globales'
df_temperaturas = pd.read_csv(archivo_temperaturas)

# Mostrar las primeras filas y los tipos de datos
print(df_temperaturas.head())
print(df_temperaturas.dtypes)

'''
Si estamos interesados solamente en las columnas 'Fecha' y 'Nueva York', podemos utilizar el argumento usecols para leer
solo esas columnas:
'''

# Leer el archivo CSV seleccionando solo algunas columnas
df_temperaturas_ny = pd.read_csv(archivo_temperaturas, usecols=['Fecha', 'Nueva York'])

# Mostrar las primeras filas del DataFrame para verificar su contenido
print(df_temperaturas_ny.head())

####################################################### Ejemplo 2 #######################################################

# Ruta al archivo CSV
archivo_precipitaciones = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_precipitaciones_globales.csv'

# Leer CSV 'precipitaciones_globales'
df_precipitaciones = pd.read_csv(archivo_precipitaciones)

# Mostrar las primeras filas y los tipos de datos
print(df_precipitaciones.head())
print(df_precipitaciones.dtypes)

'''
Si estamos interesados solamente en las columnas 'Fecha' y 'París', podemos utilizar el argumento usecols para leer
solo esas columnas:
'''

# Leer el archivo CSV seleccionando solo algunas columnas
df_precipitaciones_ny = pd.read_csv(archivo_precipitaciones, usecols=['Fecha', 'París'])

# Mostrar las primeras filas del DataFrame para verificar su contenido
print(df_precipitaciones_ny.head())