#Búsqueda lineal
def busqueda_lineal(objetivo, array):
    #Recorrer el array
    for i, numero in enumerate(array):
        #Buscar en cada elemento de la lista
        if numero == objetivo:
            return i
        else:
            print("elemento no encontrado")
    return -1
    


#Búsqueda binaria
def busqueda_binaria(array, objetivo):
    izquierda, derecha = 0, len(array) - 1
    #Ciclo while
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        #Comparar si el número es mayor o menor al que estamos buscando
        if array[medio] == objetivo:
            return medio
        #Comparar si el número es menor al objetivo
        elif array[medio] < objetivo:
            izquierda = medio + 1
        #Sino, debe ser mayor al objetivo
        else:
            derecha = medio - 1
    return -1

#Ordenar por burbuja
def burbuja(array, pasos_ordenacion=None):
    if pasos_ordenacion is not None:
        pasos_ordenacion.append(array.copy())

    #Definir el tamaño del array
    n = len(array)
    #Recorrer la lista externa
    for i in range( n - 1):
        #Recorrer la lista interna
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

#Ordenamiento por mezcla
def mezcla(array):
    #Si el arreglo no es de un solo elemento...
    if len(array) > 1:
        #Definir el medio
        medio = len(array) // 2
        #Definir la izquierda
        izq = array[:medio]
        #Definir la derecha
        der = array[medio:]

        #Llamada recursiva
        mezcla(izq)
        mezcla(der)

        #Inicializar los iteradores en 0
        i = 0
        j = 0
        k = 0

        #Ciclos while
        #Mientras la i sea menor al tamaño de la parte de la izquierda, y la j sea menor a la parte de la derecha
        while i < len(izq) and j < len(der):
            #Verificar cuál es menor y agregarlo a array
            if izq[i] < der[j]:
                array[k] = izq[i]
                i += 1
            else:
                array[k] = der[j]
                j += 1
            k += 1
        
        while i < len(izq):
            array[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            array[k] = der[j]
            j += 1
            k += 1
        
    return array

        
