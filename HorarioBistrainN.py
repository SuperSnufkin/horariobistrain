import tkinter as tk
import time

def actualizar_reloj():
    # Obtener la hora local
    ahora = time.localtime()
    normal_str = time.strftime("%H:%M:%S", ahora)
    
    # Calcular el total de minutos transcurridos (como valor fraccionario)
    M = ahora.tm_hour * 60 + ahora.tm_min + ahora.tm_sec / 60.0
    # Convertir a "horas bistrain" (cada 50 minutos normales = 1 hora Bistrain)
    B = M / 50.0  # Tiempo Bistrain en "horas" (fraccionario)
    
    b_hour = int(B)         # La parte entera son las horas Bistrain
    frac_hour = B - b_hour    # La parte fraccionaria de la hora
    
    # Los minutos Bistrain: cada hora Bistrain tiene 50 minutos
    b_min_total = frac_hour * 50
    b_min = int(b_min_total)  # Parte entera son los minutos
    b_sec = int(round((b_min_total - b_min) * 60))  # El resto en segundos
    
    # En caso de que redondee 60 segundos, ajustamos
    if b_sec == 60:
        b_sec = 0
        b_min += 1
    if b_min >= 50:
        b_min -= 50
        b_hour += 1
    
    bistrain_str = f"{b_hour:02}:{b_min:02}:{b_sec:02}"
    
    # Actualizar las etiquetas de la ventana
    label_hora_actual.config(text=f"Horario Normal: {normal_str}")
    label_hora_bistrain.config(text=f"Horario Bistrain: {bistrain_str}")
    
    ventana.after(1000, actualizar_reloj)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Bistrain")
ventana.geometry("300x150")
ventana.configure(bg="black")

# Etiqueta para el horario normal
label_hora_actual = tk.Label(ventana, text="", font=("Arial", 16), fg="white", bg="black")
label_hora_actual.pack(pady=10)

# Etiqueta para el horario Bistrain

label_hora_bistrain = tk.Label(ventana, text="", font=("Arial", 16, "bold"), fg="cyan", bg="black")
label_hora_bistrain.pack(pady=10)

# Iniciar la actualización del reloj
actualizar_reloj()
ventana.mainloop()
