'''
Filtrado

El filtrado de datos permite seleccionar elementos que cumplen ciertos criterios.
'''

import pandas as pd

# Ruta al archivo CSV
archivo_temperaturas = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_temperaturas_globales.csv'

# Leer CSV 'temperaturas_globales'
df_temperaturas = pd.read_csv(archivo_temperaturas)

'''
Queremos filtrar y ver todos los meses en los que la temperatura en Madrid fue superior a 25 grados Celsius. Para esto,
utilizaremos una operación de filtrado básico en Pandas.
'''

# Filtramos para obtener solo las filas donde la temperatura en Madrid fue mayor a 25 grados
meses_calurosos_madrid = df_temperaturas[df_temperaturas['Madrid'] > 25]

# Mostramos el resultado
print("Meses con temperaturas mayores a 25 grados en Madrid:")
print(meses_calurosos_madrid[['Fecha', 'Madrid']])