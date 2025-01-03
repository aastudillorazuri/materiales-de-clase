'''
Operaciones estadísticas

Calcular medias, medianas, máximos, mínimos, etc.
'''

import pandas as pd

# Ruta al archivo CSV
archivo_temperaturas = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_temperaturas_globales.csv'

# Leer CSV 'temperaturas_globales'
df_temperaturas = pd.read_csv(archivo_temperaturas)

'''
Por ejemplo, para obtener una idea general de las temperaturas en Berlín, podemos calcular estadísticas básicas como la media,
mediana y desviación estándar para la Serie correspondiente a Berlín.
'''

berlin_temps = df_temperaturas['Berlín']
print("Media de Temperatura en Berlín:", berlin_temps.mean())
print("Mediana de Temperatura en Berlín:", berlin_temps.median())
print("Desviación Estándar de la Temperatura en Berlín:", berlin_temps.std())