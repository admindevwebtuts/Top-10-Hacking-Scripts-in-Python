# vuln_scanner.py

# Importando las bibliotecas necesarias
import socket

# Definiendo la función de escaneo
def escanear(target_ip):
  for port in range(1, 1024): # Escaneamos los primeros 1023 puertos, ya que son puertos conocidos
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
      sock.settimeout(1) # Establecemos un tiempo de espera para el intento de conexión
      sock.connect((target_ip, port)) # Intentamos conectarnos a la IP de destino en el puerto actual
      print(f'El puerto {port} está abierto.')
      sock.close()
    except:
      print(f'El puerto {port} está cerrado.')
      pass

# Ejecutando el escáner en localhost
escanear('127.0.0.1')