import tkinter as tk
from game_header import encabezado_juego
from game_header import actualizar_turno, actualizar_fichas_rojas, actualizar_fichas_amarillas
from config import *

def iniciar_juego(board):
    boton_de_inicio = tk.Button(
        board, 
        text='Comenzar',
        bg='#DFD7F3',
        padx=30,
        pady=30,
        command=lambda: mostrar_tablero(board, boton_de_inicio)
    )
    # Posicion del boton
    boton_de_inicio.grid(
        row=0, column=0
    )
    boton_de_inicio.place(
        relx=0.5, rely=0.5, 
        anchor=tk.CENTER
    )


def mostrar_tablero(board, boton):
    boton.destroy()
    encabezado_juego(board)
    botones_para_columnas(board)

    for row in range(n_filas):
        for col in range(n_columnas):
            cell = tk.Label(
                board, 
                width=6, height=2, 
                relief="solid", 
                borderwidth=1
            )
            cell.grid(
                row=row+2,  # row+2 to account for info frame and column buttons
                column=col, 
                padx=0, 
                pady=1
            )



def botones_para_columnas(board):
    # Create column buttons
    for col in range(n_columnas):
        button = tk.Button(
            board,
            text="↓",
            width=6,
            command=lambda col=col: [colocar_ficha(col, board)]
        )
        button.grid(row=1, column=col, padx=5)
        botones_de_columnas.append(button)



def colocar_ficha(col, board):
    global turno, fichas_rojas, fichas_amarrillas

    for row in range(n_filas-1, -1, -1):
        if tablero_de_juego[row][col] == 0:
            tablero_de_juego[row][col] = turno
            color = 'red' if turno == 1 else 'yellow'
            cell = tk.Label(
                board, 
                width=6, height=2, 
                relief="solid", 
                borderwidth=1, 
                bg=color
            )
            cell.grid(
                row=row+2,  # row+2 to account for info frame and column buttons
                column=col, 
                padx=0, 
                pady=1
            )
            turno = 3 - turno  # Switch turn between 1 and 2
            actualizar_turno(turno)
            if color == 'red':
                fichas_rojas = fichas_rojas - 1
                actualizar_fichas_rojas(fichas_rojas)
            else:
                fichas_amarrillas = fichas_amarrillas - 1
                actualizar_fichas_amarillas(fichas_amarrillas)
            break