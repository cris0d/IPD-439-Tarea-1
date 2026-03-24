import serial
import matplotlib.pyplot as plt
import numpy as np
import sys

# --- CONFIGURACIÓN ---
PUERTO = 'COM4'
BAUDIOS = 115200
N_MUESTRAS = 200 

# Variable global para controlar el estado de la ventana
ventana_abierta = True

def al_cerrar(event):
    """Función que se ejecuta al cerrar la ventana de la gráfica."""
    global ventana_abierta
    ventana_abierta = False
    print("Ventana cerrada por el usuario.")
    plt.close('all')

# Configuración de la gráfica
plt.ion()
fig, ax = plt.subplots(figsize=(10, 5))
fig.canvas.mpl_connect('close_event', al_cerrar) # Conectar evento de cierre

datos = np.zeros(N_MUESTRAS)
linea, = ax.plot(datos, color='r', lw=1.5)

ax.set_ylim(0, 5000)
ax.set_xlim(0, N_MUESTRAS)
ax.set_title("Captura STM32 - Esperando pulsación de botón...")
ax.grid(True)

def esperar_y_leer_bloque(ser):
    """Espera a que llegue el primer byte y luego lee el bloque completo."""
    nuevo_buffer = []
    
    # 1. Espera activa hasta que el STM32 envíe algo (botón presionado)
    while ventana_abierta and ser.in_waiting == 0:
        fig.canvas.flush_events()
        plt.pause(0.05) # Pausa larga mientras no hay datos para no consumir CPU
        if not ventana_abierta: return None

    print("Recibiendo ráfaga de datos...")
    
    # 2. Leer buffer
    while ventana_abierta and len(nuevo_buffer) < N_MUESTRAS:
        if ser.in_waiting > 0:
            linea_raw = ser.readline().decode('utf-8').strip()
            if linea_raw:
                try:
                    nuevo_buffer.append(int(linea_raw))
                except ValueError:
                    continue
        
        fig.canvas.flush_events()
        plt.pause(0.001)
        
    return nuevo_buffer

try:
    with serial.Serial(PUERTO, BAUDIOS, timeout=0.1) as ser:
        print(f"Conectado a {PUERTO}. Presione el botón en la placa...")
        
        while ventana_abierta:
            ser.reset_input_buffer()
            
            # Esperamos boton
            datos_recibidos = esperar_y_leer_bloque(ser)
            
            if datos_recibidos and ventana_abierta:
                linea.set_ydata(datos_recibidos)
                ax.set_title("Lectura de ADC - Botón presionado")
                plt.draw()
                print(f"Gráfica actualizada con {len(datos_recibidos)} puntos.")

except serial.SerialException as e:
    print(f"Error de puerto: {e}")
except KeyboardInterrupt:
    print("\nScript detenido por teclado.")
finally:
    print("Programa finalizado.")