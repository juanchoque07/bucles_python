# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores

colores = ['rojo', 'naranja', 'verde', 'azul']
for color in colores:
    print(color)

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

for i in range(len(colores)):
    print("Para el codigo",i,"el color correspondiente es",colores[i])    

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...
codigo = int(input("ingrese un numero entre 0 y 3\n"))

for i in range(len(colores)):
    if i == codigo:
        
        print("El color referido es ",colores[i])


print("terminamos!")