if 10 > 9: # True
    print('Es correcto')

if True:
    print('Es correcto')

x = True
if x:
    print('Es correcto')

if 5 == 2: # False
    print('Es correcto') # No se ejecuta

if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
else:
    print('No sé qué animal tienes')

mascota = 'perro'
if mascota == 'gato': # No ingresa a la línea de ejecución
    print('Tienes un gato')
elif mascota == 'perro': # Verifica y ejecuta esta línea
    print('Tienes un perro')
else:
    print('No sé qué animal tienes')

mascota = 'pez'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé qué animal tienes')

edad = 16
calificación = 9
if edad < 18:
    print('Eres menor de edad')
    if calificación >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')