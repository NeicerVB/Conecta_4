import tkinter as tk

# Variables globales
n_filas = 6
n_columnas = 7
fichas_rojas = 21
fichas_amarrillas = 21
turno = 1
contador_de_partidas_ganadas_rojo = 0
contador_de_partidas_ganadas_amarillo = 0
tablero = [[0 for _ in range(n_columnas)] for _ in range(n_filas)]
column_buttons = []

# Funciones
def desactivar_botones():
    for button in column_buttons:
        button.config(state=tk.DISABLED)

def colocar_ficha(col):
    global turno, fichas_rojas, fichas_amarrillas
    for row in range(n_filas-1, -1, -1):
        if tablero[row][col] == 0:
            tablero[row][col] = turno
            color = 'red' if turno == 1 else 'yellow'
            cell = tk.Label(
                root, 
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
            turno_label.config(text=f"Turno: {'Rojo' if turno == 1 else 'Amarillo'}")
            if color == 'red':
                fichas_rojas -= 1
                fichas_rojas_label.config(text=f"Fichas Rojas: {fichas_rojas}")
            else:
                fichas_amarrillas -= 1
                fichas_amarillas_label.config(text=f"Fichas Amarillas: {fichas_amarrillas}")
            break

def botones_para_columnas(root):
    for col in range(n_columnas):
        button = tk.Button(
            root,
            text="↓",
            width=6,
            command=lambda col=col: [colocar_ficha(col)]
            # command=lambda: colocar_ficha(col)
        )
        button.grid(row=1, column=col, pady=5)
        column_buttons.append(button)

def mostrar_tablero(root, info_frame):
    encabezado_juego(info_frame)
    botones_para_columnas(root)

    for row in range(n_filas):
        for col in range(n_columnas):
            cell = tk.Label(
                root, 
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
    start_button.destroy()  # Remove start button after clicking


def encabezado_juego(info_frame):
    # Etiquetas para el estado del juego
    turno_label = tk.Label(info_frame, text=f"Turno: {'Rojo' if turno == 1 else 'Amarillo'}")
    turno_label.grid(row=0, column=0, padx=10)

    fichas_rojas_label = tk.Label(info_frame, text=f"Fichas Rojas: {fichas_rojas}")
    fichas_rojas_label.grid(row=0, column=1, padx=10)

    fichas_amarillas_label = tk.Label(info_frame, text=f"Fichas Amarillas: {fichas_amarrillas}")
    fichas_amarillas_label.grid(row=0, column=2, padx=10)

    score_label = tk.Label(info_frame, text=f"Rojo: {contador_de_partidas_ganadas_rojo} - Amarillo: {contador_de_partidas_ganadas_amarillo}")
    score_label.grid(row=0, column=3, padx=10)



# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Conecta 4")
root.geometry("450x300")
root.resizable(False, False)

# Crear frame para la información del juego
info_frame = tk.Frame(root)
info_frame.grid(row=0, column=0, columnspan=7, pady=5)

# Crear botón de inicio y centrarlo
start_button = tk.Button(
    root, 
    text="Iniciar juego", 
    command=lambda: mostrar_tablero(root, info_frame)
)
start_button.place(
    relx=0.5, rely=0.5, 
    anchor=tk.CENTER
)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()