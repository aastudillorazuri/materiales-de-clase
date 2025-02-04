'''
-- ¿Qué es una Serie?

Una Serie en Pandas es similar a una columna en una tabla.

Es un array unidimensional que puede contener datos de cualquier tipo.

Ejemplo

Crear una Serie de Pandas a partir de una lista:
'''

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

'''
-- Etiquetas

Si no se especifica nada, los valores se etiquetan con su número de índice.
El primer valor tiene índice 0, el segundo 1, y así sucesivamente.

Estas etiquetas pueden usarse para acceder a valores específicos.

Ejemplo

Obtener el primer valor de la Serie:
'''

print(myvar[0])

'''
-- Crear Etiquetas

Puedes definir tus propias etiquetas utilizando el argumento index.

Ejemplo

Crear una Serie con etiquetas personalizadas:
'''

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

'''
Una vez creadas las etiquetas, puedes acceder a los valores usando dichas etiquetas.

Ejemplo

Obtener el valor de "y":
'''

print(myvar["y"])

'''
-- Objetos Clave/Valor como Series

También puedes usar un diccionario (clave/valor) para crear una Serie.

Ejemplo

Crear una Serie a partir de un diccionario:
'''

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

'''
Nota: Las claves del diccionario se convierten en etiquetas.

Si deseas incluir solo algunos elementos del diccionario, usa el argumento index para especificar las claves deseadas.

Ejemplo

Crear una Serie con solo los datos de "day1" y "day2":
'''

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index=["day1", "day2"])

print(myvar)

'''
-- DataFrames

En Pandas, los conjuntos de datos suelen representarse como tablas multidimensionales, llamadas DataFrames.

Una Serie es como una columna en una tabla.
Un DataFrame es toda la tabla.

Ejemplo

Crear un DataFrame a partir de dos Series:
'''

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)