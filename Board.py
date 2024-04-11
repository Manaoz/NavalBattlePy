import numpy as np
import random

def posicion_barcos(): #Definimos la posición de los barcos dentro del tablero

    tablero = np.full((10, 10), ' ')        #Creamos nuestro tablero, de tamaño 10x10 vacío
    barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] #Creamos una lista donde integramos las esloras de nuestros 10 barcos

    
    counter = len(barcos)  #Hacemos conteo con len en la lista anterior que hemos creado, para que vaya iterando por cada eslora de la lista

    while counter > 0:  #Mientras el conteo de los barcos, que son 10 en total, no sea 0, recorremos la lista para integrarlos en el tablero

        """
        Creamos las orientaciones de forma aleatorias, dando las orientaciones:
            # Oe = Oeste
            # S = Sur
            # N = Norte
            # E = Este   
        """
        orient = random.choice(['Oe', 'S', 'N', 'E']) 

        # Le decimos que nos de una coordenada en un rango hasta 10 (como el maximo de nuestro tablero),
        # con un tamaño de 2, es decir, 2 numeros que serán nuestras coordenadas: la fila y la columna.

        current_pos = np.random.randint(10, size = 2)
        fila = current_pos[0] # Designamos que en los 2 valores que nos de de posicion, fila es el primer valor
        columna = current_pos[1] # Y a su vez, decimos que el valor de la columna es el segundo numero de la posicion
        
        
        for i in barcos: # Para cada tamaño de la eslora en los barcos
            if orient == 'Oe' and (i <= len(range(columna, 0, -1))) and ('O' not in tablero[fila, columna:columna - i:-1]):
                tablero[fila, columna:columna - i:-1] = 'O'
                counter = counter - 1
                barcos.remove(i)
            elif orient == 'E' and (i <= len(range(columna, 10))) and ('O' not in tablero[fila, columna:columna + i]):
                tablero[fila, columna:columna + i] = 'O'
                counter = counter - 1
                barcos.remove(i)
            elif orient == 'S' and (i <= len(range(fila, 10))) and ('O' not in tablero[fila:fila + i, columna]):
                tablero[fila: fila + i, columna] = 'O'
                counter = counter - 1
                barcos.remove(i)
            elif orient == 'N' and (i <= len(range(fila, 0, -1))) and ('O' not in tablero[fila:fila - i:-1, columna]):
                tablero[fila:fila - i:-1, columna] = 'O'
                counter = counter - 1
                barcos.remove(i)
    return tablero
posicion_barcos()
