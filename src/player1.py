import jugador2
import numpy as np
import time

tablero = np.full((10, 10), ' ')
tablero_auto_disp = tablero.copy()
tablero_jugador_disp = tablero.copy()

tablero_vacio = np.full((10,10,), " ") 
tablero_vacio2 = np.full((10,10,), " ")

def disparo_player1(tablero_jugador_disp, tablero_vacio,tablero_auto_disp,tablero_vacio2):
    while 'O' in tablero_jugador_disp and 'O' in tablero_auto_disp: 
        print('Este es el Tablero de la maquina\n',tablero_vacio)
        print('Este es nuestro tablero\n',tablero_auto_disp)
        try:
            x = int(input('J1, Introduce coordenada de la fila del 0 al 9: '))
            if x < 0 or x > 9:
                x = int(input('Num. no valido, tira otra vez coordenada de la fila del 0 al 9: '))
                continue
            y = int(input('J1, Introduce coordenada de columna del 0 al 9: '))
            if y < 0 or y > 9:
                y = int(input('Num. no valido, tira otra vez coordenada de columna del 0 al 9: '))
                continue
        
    
            if tablero_jugador_disp[x, y] == 'O':  
                tablero_jugador_disp[x, y] = 'X'
                tablero_vacio[x, y] = 'X'
                print('Tablero de la maquina"\n", Has dado en el BLANCO!\n')
                
                continue
            if tablero_jugador_disp[x, y] == ' ':
                tablero_jugador_disp[x, y] = '-'
                tablero_vacio[x, y] = '-'
                print("Tablero de la maquina\n", 'Has dado en el AGUA!\n', tablero_vacio)
                time.sleep(2)
                jugador2.disparo_player2(tablero_auto_disp,tablero_vacio2,tablero_jugador_disp, tablero_vacio)

            else:
                continue
        except ValueError:
            print("Introduzca un valor numérico entre 0 y 9 por favor")