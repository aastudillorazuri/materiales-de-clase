mi_bool = 4 < 5 < 6 
print(mi_bool) # True

mi_bool = 4 < 5 > 6
print(mi_bool) # False

mi_bool = 4 < 5 and 5 > 6
print(mi_bool) # False

mi_bool = 4 < 5 and 5 == 2 + 3
print(mi_bool) # True

mi_bool = (4 < 5) and (5 == 2 + 3)
print(mi_bool) # True

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool) # True

mi_bool = 10 == 10 or 3 == 3
print(mi_bool) # True

mi_bool = 1 == 10 or 3 == 30
print(mi_bool) # False

texto = 'Esta frase es breve'
mi_bool = 'frase' in texto
print(mi_bool) # True

texto = 'Esta frase es breve'
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool) # True

texto = 'Esta frase es breve'
mi_bool = ('frase' in texto) and ('python' in texto)
print(mi_bool) # False

texto = 'Esta frase es breve'
mi_bool = ('frase' in texto) or ('python' in texto)
print(mi_bool) # True

mi_bool = 'a' == 'a'
print(mi_bool) # True

mi_bool = not 'a' == 'a'
print(mi_bool) # False

mi_bool = not ('a' == 'a')
print(mi_bool) # False

mi_bool = not ('a' != 'a')
print(mi_bool) # True