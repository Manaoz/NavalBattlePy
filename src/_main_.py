import numpy as np
import PosicionBarcos
import jugador1
import jugador2

import time
barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
tablero1 = PosicionBarcos.posicion_barcos()
tablero2 = PosicionBarcos.posicion_barcos()

tablero_auto_disp = tablero1.copy()
tablero_jugador_disp = tablero2.copy()
print(0,1,2,3,4,5,6,7,8,9)
tablero_vacio = np.full((10,10,), ' ')
    
tablero_vacio2 = np.full((10,10,), ' ')


print('Bienvenido a HUNDIR LA FLOTA')
print('Tu misión es acabar con todos los barcos del contricante')

menu = int(input('¿Qué te gustaría hacer?\n 1 - JUGAR \n 2 - SALIR  '))

while menu == 1:
    time.sleep(1)
    PosicionBarcos.posicion_barcos()

    jugador1.disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2)
    jugador2.disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio)

while menu == 2:
    exit('HASTA LA PRÓXIMA')


