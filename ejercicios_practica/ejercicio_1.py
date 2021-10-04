# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

print("Ejercicios con bucles while")

xx = 0
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración
condicion = False
# Variable "x" cambiada por variable "xx".
while xx < 6:
    xx += 1
    print("xx vale", xx)

# reemplace "condicion" por lo que crea necesario
# Se crea variable "s"
s = int(input("ingrese el numero limite de accion\n"))
x = 0
while x < s :
    x += 1    
    print("Valor de x =", x)
    # Coloque la línea de código para que "x" incremente "1"

print("cuenta a cero xs")
xs = 5 # variable "x" modificada a "xs"

# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración
while xs >= 0:
    xs -= 1
    print("el valor de xs es",xs)
            

print("ejercicio con variable xf")

xf = 0 #otra modificacion de variable "x" por "xf" 

while xf<10:    # reemplace "condicion" por lo que crea necesario
    print("Valor de xf =", xf)
    xf += 1
    # Coloque la línea de código para que "x" decremente "1"

print("terminamos!")
