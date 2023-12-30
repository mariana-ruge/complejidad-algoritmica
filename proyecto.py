#importar módulos
import os
os.system('cls')
from algoritmos import busqueda_lineal, busqueda_binaria, burbuja, mezcla
#importar módulos
import random

#Importa bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_file

def mostar_grafico(lista, titulo):
    #Archivo de gráficos
    output_file('graficado.html')
    #Tamaño del canvas para la gráfica
    fig = figure(title=titulo, width=800, height=400)
    #Agregando barras al gráfico
    fig.vbar(x =list( range(len(lista))), top=lista, width=0.9, color="blue")
    #Ejes del gráfico
    fig.xaxis.axis_label = "Índice"
    fig.yaxis.axis_label = "Valor"
    show(fig)



def main():
    #Generar una lista aleatoria para el juego
    #random.sample -> toma una pequeña parte del rango definido, en este caso de 10 números y devuelve una lista de estos
    #sample(range(primer elemento del rango, segundo elemento del rango), tamaño de la lista)
    lista_desordenada = random.sample(range(1, 101), 10)
    print("Lista desordenada: ", lista_desordenada)

    #Preguntar al usuario que algoritmo  para ordenar desea usar
    #Lowe es para tomar la opción digitada en minúscula
    opcion = input("\n ¿Qué algoritmo deseas usar para ordenar? (b: burbuja, m: mezcla) ").lower()

    #Lista de listas para almacenar en cada paso
    pasos_ordenacion = [lista_desordenada.copy()]

    #Ordenar la lista
    if opcion == 'b':
        #llamar a la función burbuja y pasarle como argumentos la lista desordenada e imprimirla
        lista_ordenada = burbuja(lista_desordenada, pasos_ordenacion)
    elif opcion == 'm':
        #llamar a la función mezcla y pasarle como argumentos la lista desordenada e imprimirla
        lista_ordenada = mezcla(lista_desordenada)
    else:
        print("Opción inválida")

    #Mostrar el gráfico
    mostar_grafico(pasos_ordenacion[-1], "Progreso de Ordenación")

    print('Lista ordenada:', lista_ordenada)

    #Buscar en la lista
    opcion_busqueda = input("\n ¿Qué algoritmo deseas para hacer la búsqueda? (l: lineal, b: binaria)").lower()

    #Declarar el objetivo
    objetivo = int(input('Ingresa el número a buscar: '))

    #Comparar las opciones
    if opcion_busqueda == 'l':
        #obtener la posición para lineal
        posicion = busqueda_lineal(objetivo, lista_ordenada)
    elif opcion_busqueda == 'b':
        #obtener la posición para binaria
        posicion = busqueda_binaria(lista_ordenada, objetivo)
    else:
        print('Opción inválida')

    #Mostrar el gráfico interactivo de la ordenación
    #Identificar los elementos encontrados
    #Si es diferente de 1 significa que existe, sino, no existe
    if posicion != 1:
        print('\n El número {} se encuentra en la posición {}.'.format(objetivo, posicion))
    else:
        print('\n No se encontró el número {}.'.format(objetivo))



if __name__ == '__main__':
    main()
