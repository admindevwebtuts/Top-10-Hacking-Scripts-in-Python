import socket
import threading

# Definir una función para escanear un solo puerto
def escanear(target_ip, puerto, bloqueo):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, puerto))
        bloqueo.acquire()   # Adquirir el bloqueo antes de imprimir
        print(f'El puerto {puerto} está abierto.')
        bloqueo.release()   # Liberar el bloqueo después de imprimir
        sock.close()
    except:
        pass

# Crear un objeto de bloqueo
bloqueo = threading.Lock()

# Escanear puertos del 1 al 1024
for puerto in range(1, 1024):
    hilo = threading.Thread(target=escanear, args=('127.0.0.1', puerto, bloqueo))
    hilo.start()