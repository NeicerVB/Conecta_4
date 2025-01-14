import tkinter as tk
from config import *

# Declarar las variables globales
turno_label = None
fichas_rojas_label = None
fichas_amarillas_label = None
score_label = None

def encabezado_juego(board):
    global turno_label, fichas_rojas_label, fichas_amarillas_label, score_label

    info_frame = tk.Frame(board)
    info_frame.grid(row=0, column=0, columnspan=7, pady=5)

    turno_label = tk.Label(info_frame, text=f"Turno: {'Rojo' if turno == 1 else 'Amarillo'}", width=14)
    turno_label.grid(row=0, column=0, padx=10)

    fichas_rojas_label = tk.Label(info_frame, text=f"Fichas Rojas: {fichas_rojas}", width=14)
    fichas_rojas_label.grid(row=0, column=1)

    fichas_amarillas_label = tk.Label(info_frame, text=f"Fichas Amarillas: {fichas_amarrillas}", width=14)
    fichas_amarillas_label.grid(row=0, column=2)

    score_label = tk.Label(info_frame, text=f"Rojo: {contador_de_partidas_ganadas_rojo} - Amarillo: {contador_de_partidas_ganadas_amarillo}", width=14)
    score_label.grid(row=0, column=3, padx=10)
    

# Ahora puedes modificar las etiquetas fuera de la función
def actualizar_turno(nuevo_turno):
    global turno_label
    turno_label.config(text=f"Turno: {'Rojo' if nuevo_turno == 1 else 'Amarillo'}")

def actualizar_fichas_rojas(nuevas_fichas_rojas):
    global fichas_rojas_label
    fichas_rojas_label.config(text=f"Fichas Rojas: {nuevas_fichas_rojas}")

def actualizar_fichas_amarillas(nuevas_fichas_amarillas):
    global fichas_amarillas_label
    fichas_amarillas_label.config(text=f"Fichas Amarillas: {nuevas_fichas_amarillas}")

def actualizar_score(nuevo_score_rojo, nuevo_score_amarillo):
    global score_label
    score_label.config(text=f"Rojo: {nuevo_score_rojo} - Amarillo: {nuevo_score_amarillo}")