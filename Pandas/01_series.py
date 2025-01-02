'''
Series

Una Serie en Pandas es una estructura de datos unidimensional que puede contener cualquier tipo de datos (enteros,
cadenas, flotantes, objetos de Python, etc.). Cada elemento de una Serie se asocia con un índice, que es como una
etiqueta o identificador único para el elemento. 
'''

import pandas as pd

# Creación de una Serie a partir de una lista
temperaturas1 = pd.Series([22, 24, 19, 23, 25, 26])

print(temperaturas1)

# Creación de una Serie con índice personalizado
temperaturas = pd.Series([22, 24, 19, 23, 25, 26], index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'])

print(temperaturas)