import random
import jugador1
import numpy as np
import time
tablero = np.full((10, 10), ' ')
tablero_auto_disp = tablero.copy()
tablero_jugador_disp = tablero.copy()

tablero_vacio = np.full((10,10,), " ") 
tablero_vacio2 = np.full((10,10,), " ")

def disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio):
   
    while 'O' in tablero_auto_disp and 'O' in  tablero_jugador_disp:
        
        x = random.randint(0,9)
        y = random.randint(0,9)

        if tablero_auto_disp[x, y] == 'O':
            tablero_auto_disp[x, y] = 'X'
            tablero_vacio2[x, y] = 'X'
            print("Tablero de la maquina\n", 'El adversario ha dado en el BLANCO!\n', tablero_auto_disp)
            continue
        elif tablero_auto_disp[x, y] == ' ':
            tablero_auto_disp[x, y] = '-'
            tablero_vacio2[x, y] = '-'
            print("Tablero de la maquina\n", 'La maquina ha dado en el AGUA!\n', tablero_auto_disp)
            time.sleep(2)
            jugador1.disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2)
        else:
            continue