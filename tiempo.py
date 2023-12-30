import os
import sys
os.system('cls')
import time
sys.set_int_max_str_digits(10000)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def fatorial_recursivo(n):
    if n == 1:
        return 1
    
    return n * fatorial_recursivo(n - 1)


n = 900

#Medir el tiempo de ejecución
comienzo = time.time()
print("**Resultado del Factorial")
print(factorial(n))
final = time.time()
print("**Medida del tiempo de ejecución**")
print(final - comienzo)

print("**Ejecutando otra operación del factorial**")
print(fatorial_recursivo(n))

comienzo = time.time()
print(fatorial_recursivo(n))
final = time.time()
print("**Resultado del tiempo de ejecución del factorial recursivo**")
print(final - comienzo)