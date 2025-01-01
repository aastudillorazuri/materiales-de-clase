"""
nombres = ['Juan', 'Ana', 'Carlos', 'Belén', 'Fran']

por cada elemento en nombres:
    imprimir("Hola")

for elemento in nombres:
    print("Hola")
> Hola
> Hola
> Hola
> Hola
> Hola

for elemento in nombres:
    print("Hola " + elemento)
> Hola Juan
> Hola Ana
> Hola Carlos
> Hola Belén
> Hola Fran
"""

lista = ['a', 'b', 'c', 'd']

for letra in lista:
    print(letra)

for letra in lista:
    print('Letra: ' + letra)

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']

for nombre in lista:
    if nombre.startswith('L'):
        print(nombre) # Laura, Luis

for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

numeros = [1, 2, 3, 4, 5]

mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor) # 15

mi_valor = 0
for numero in numeros:
    mi_valor += numero
    print(mi_valor) # 1, 3, 6, 10, 15

palabra = 'Python'

for letra in palabra:
    print(letra) # P, y, t, h, o, n

palabra = 'Python es genial'

for letra in palabra:
    print(letra)

for letra in 'Python':
    print(letra)

for letra in [1, 2, 3]:
    print(letra)

for letra in (1, 2, 3):
    print(letra)

for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto) # [1, 2], [3, 4], [5, 6]

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a) # 1, 3, 5

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b) # 1, 2, 3, 4, 5, 6

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic:
    print(item) # clave1, clave2, clave3

# El método items() es una función que devuelve una lista de tuplas que contienen los pares de clave y valor de un diccionario
for item in dic.items():
    print(item) # ('clave1', 'a'), ('clave2', 'b'), ('clave3', 'c')

# El método values() devuelve una lista con todos los values o valores del diccionario
for item in dic.values():
    print(item) # a, b, c

for a, b in dic.items():
    print(a, b) # clave1 a, clave2 b, clave3 c