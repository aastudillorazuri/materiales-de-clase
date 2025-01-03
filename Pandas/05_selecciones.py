'''
Selección de columnas específicas
'''

import pandas as pd

# Ruta al archivo CSV
archivo_temperaturas = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_temperaturas_globales.csv'

# Leer CSV 'temperaturas_globales'
df_temperaturas = pd.read_csv(archivo_temperaturas)

# Supongamos que queremos seleccionar la columna 'Londres' del DF df_temperaturas:
print(df_temperaturas['Londres'])