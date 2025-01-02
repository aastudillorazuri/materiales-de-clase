print("La Witsi Witsi Araña subió a su telaraña.")
print() # La invocación vacía de print() genera una línea vacía o (esta interpretación también es correcta) genera una nuevalínea.
print("Vino la lluvia y se la llevó.")

'''
La barra invertida (\) tiene un significado muy especial cuando se usa dentro de cadenas - se llama carácter de escape.
La palabra escape significa que la serie de caracteres en la cadena se escapa por un momento (un momento muy breve) para introducir una inclusión especial.
En otras palabras, la barra invertida no significa nada en sí misma, sino que es solo una especie de anuncio de que el siguiente carácter después de la barra invertida también tiene un significado diferente.
La letra n colocada después de la barra invertida proviene de la palabra new line.
Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nueva línea, que insta a la consola a iniciar una nueva línea de salida.
'''

print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

'''
Si deseas colocar solo una barra invertida dentro de una cadena, no olvides su naturaleza de escape - tienes que duplicarla.
Por ejemplo, una invocación como esta provocará un error:

print("\")
'''

# También vale la pena intentar alimentar a la función print() con más de un argumento:

print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")

'''
Dos conclusiones emergen de este ejemplo:

La función print() invocada con más de un argumento los muestra todos en una sola línea.
La función print() pone un espacio entre los argumentos de salida por iniciativa propia.
'''

