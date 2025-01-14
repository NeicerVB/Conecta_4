import tkinter as tk
from game_logic import iniciar_juego

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

board = tk.Tk()

# Configuraciones del tablero
board.title("Conecta 4")
board.resizable(False, False)

# Centrar la ventana
centrar_ventana(board, 470, 300)

# Boton para iniciar el juego
iniciar_juego(board)

board.mainloop()