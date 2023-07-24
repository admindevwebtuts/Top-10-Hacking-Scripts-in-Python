import socket
import threading

target = input("Ingrese la dirección IP objetivo para escanear: ")
print("Ingrese el rango de puertos a escanear (formato: inicio-fin):")
start_port, end_port = map(int, input().split('-'))

def port_scanner(port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    con = s.connect((target,port))
    print(f'El puerto {port} está abierto')
    con.close()
  except:
    pass

for port in range(start_port, end_port+1):
  thread = threading.Thread(target=port_scanner, args=(port,))
  thread.start()