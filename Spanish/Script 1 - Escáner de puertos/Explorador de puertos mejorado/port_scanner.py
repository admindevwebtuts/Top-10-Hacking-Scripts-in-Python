import socket
import threading

# Entrada del usuario para la dirección IP objetivo
objetivo = input("Ingrese la dirección IP objetivo para escanear: ")

def escaner_puertos(puerto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        con = s.connect((objetivo,puerto))
        print(f'El puerto {puerto} está abierto')
        con.close()
    except:
        pass

# Escaneo de puertos utilizando hilos para mayor velocidad
for puerto in range(1,1025):
    hilo = threading.Thread(target=escaner_puertos, args=(puerto,))
    hilo.start()