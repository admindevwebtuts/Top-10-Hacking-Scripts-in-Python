import socket

destino = 'localhost'
puerto = 80
# Crear un objeto de socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Establecer un tiempo de espera
s.settimeout(5)

def escaner_puertos(puerto):
  if s.connect_ex((destino, puerto)):
    print("El puerto está cerrado")
  else:
    print("El puerto está abierto")

# Escanear los primeros 1024 puertos
for puerto in range(0, 1025):
  print(puerto)
  escaner_puertos(puerto)

escaner_puertos(puerto)