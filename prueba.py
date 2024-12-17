
n_filas = 6
n_columnas = 7

# Definir la cantidad de fichas rojas y amarillas
fichas_rojas = 21
fichas_amarrillas = 21

# Definir el turno del jugador
turno = 1
contador_de_partidas_ganadas_rojo = 0
contador_de_partidas_ganadas_amarillo = 0



import tkinter as tk

root = tk.Tk()
root.title("Conecta 4")


# Create frame for game info
info_frame = tk.Frame(root)
info_frame.grid(row=0, column=0, columnspan=7, pady=5)

# Labels for game status
turno_label = tk.Label(info_frame, text=f"Turno: {'Rojo' if turno == 1 else 'Amarillo'}")
turno_label.grid(row=0, column=0, padx=10)

fichas_rojas_label = tk.Label(info_frame, text=f"Fichas Rojas: {fichas_rojas}")
fichas_rojas_label.grid(row=0, column=1, padx=10)

fichas_amarillas_label = tk.Label(info_frame, text=f"Fichas Amarillas: {fichas_amarrillas}")
fichas_amarillas_label.grid(row=0, column=2, padx=10)

score_label = tk.Label(info_frame, text=f"Rojo: {contador_de_partidas_ganadas_rojo} - Amarillo: {contador_de_partidas_ganadas_amarillo}")
score_label.grid(row=0, column=3, padx=10)


# Create start button and center it
start_button = tk.Button(root, text="Iniciar juego")
start_button.grid(row=7, column=3, pady=10)

def botones_para_columnas(root):
    # Create column buttons
    for col in range(n_columnas):
        button = tk.Button(
            root,
            text="↓",
            width=5
        )
        button.grid(row=1, column=col, pady=5)

def mostrar_tablero(root):
    botones_para_columnas(root)

    # Create grid cells
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

start_button.config(command=lambda: mostrar_tablero(root))