# Importamos Pandas
import pandas as pd

# Importar "211_ventas_autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv(r'C:\Users\USER\Documents\Data\materiales-de-clase\Python TOTAL\211_ventas_autos.csv')
print(ventas_autos)

# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
import matplotlib.pyplot as plt

ventas_autos['Kilometraje'].plot(kind = 'line')
plt.show()

# ¿Puede que un gráfico más apropiado en este caso sea un histograma?
ventas_autos['Kilometraje'].hist()
plt.show()

# Intentamos graficar la columna de precios
ventas_autos['Precio (USD)'] = ventas_autos['Precio (USD)'].str.replace('[,\$\.]', '', regex = True)  # Elimina comas, dólares y puntos
ventas_autos['Precio (USD)'] = pd.to_numeric(ventas_autos['Precio (USD)'], errors = 'coerce')  # Convierte a numérico, reemplaza errores por NaN
ventas_autos['Precio (USD)'] = ventas_autos['Precio (USD)'] / 100  # Escala los valores dividiéndolos por 100
print(ventas_autos)

ventas_autos['Precio (USD)'].plot(kind = 'line')
plt.show()