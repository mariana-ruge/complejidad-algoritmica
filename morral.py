import os
os.system('cls')
#Capacidad -> ¿Cuántos objetos le caben al morral?
#Pesos -> ¿Cuánto pesa cada objeto en el morral?

def morral(tamanio, lista_pesos, lista_valores, n):
    #Caso base  -> No hay más espacio, o no hay mas elementos
    if n == 0 or tamanio == 0:
        return 0
    
    #Si el peso de los objetos es menor que el del morral, se puede agregar 
    if lista_pesos[n - 1] > tamanio:
        return morral(tamanio, lista_pesos, lista_valores, n-1)
    
    return max(lista_valores[n - 1] + morral(tamanio - lista_pesos[n-1], lista_pesos, lista_valores, n - 1), morral(tamanio, lista_pesos, lista_valores, n - 1))



def obtener_datos():
    #Obtener los datos
    input_valores = input('ingresa los valores que van en el morral, separado por comas :')
    input_pesos = input('ingresa los pesos de cada valor que va en el morral, separado por comas :')
    tamanio = int(input('¿Cuál es el tamaño de la maleta?'))
    #Pasar de Strings a listas
    valores = input_valores.split(',')
    pesos = input_pesos.split(',')
    #Crear las listas de enteros para los valores y pesos
    lista_valores = []
    lista_pesos = []
    
    #Pasar los valores a enteros
    for i in valores:
        val_int = int(i)
        lista_valores.append(val_int)
        
    #Pasar los pesos a enteros
    for i in pesos:
        val_pint = int(i)
        lista_pesos.append(val_pint)

    #Imprimir las listas
    print(lista_valores)
    print(lista_pesos)
    print(tamanio)

    #Tamaño de la lista de los valores
    n = len(lista_valores)

    #Llamada a la función morral
    resultado = morral(tamanio, lista_pesos, lista_valores, n)
    print(resultado)

    return tamanio, lista_pesos, lista_valores, n




if __name__ == '__main__':
    obtener_datos()
    