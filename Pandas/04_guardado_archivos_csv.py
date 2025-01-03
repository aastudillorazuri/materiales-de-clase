'''
Guardado de datos

Una vez que has realizado el análisis o manipulación de tus datos (lo cual aprenderás en detalle más adelante), es posible
que quieras guardar tus resultados. Pandas facilita la exportación de DataFrames a varios formatos de archivo. Para guardar
datos en formato CSV, puedes utilizar la función df.to_csv().
'''

import pandas as pd

# Ruta al archivo CSV
archivo_temperaturas = r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\03_temperaturas_globales.csv'

# Leer CSV 'temperaturas_globales'
df_temperaturas = pd.read_csv(archivo_temperaturas)

# Suponiendo que df_temperaturas ya está definido y modificado con una nueva columna
df_temperaturas.to_csv(r'C:\Users\USER\Documents\Data\materiales-de-clase\Pandas\04_temperaturas_modificadas.csv', index=False)

'''
Nota: 

index=False: es un parámetro opcional que indica a Pandas no escribir el índice del DataFrame en el archivo. Esto es útil
cuando el índice no contiene información relevante.
'''