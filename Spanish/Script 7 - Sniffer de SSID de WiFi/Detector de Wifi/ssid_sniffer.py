import socket
import struct
import sys

def crear_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('No se pudo crear el socket. Código de error: ' + str(msg[0]) + ' Mensaje ' + msg[1])
        sys.exit()

    return s

def espiar(s):
    while True:
        paquete = s.recvfrom(65565)
        paquete = paquete[0]
        # Analizamos el paquete usando struct
        encabezado_ip = paquete[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s' , encabezado_ip)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        longitud_iph = ihl * 4
        ttl = iph[5]
        protocolo = iph[6]
        dir_origen = socket.inet_ntoa(iph[8])
        dir_destino = socket.inet_ntoa(iph[9])

        # Mostramos parte de la información que analizamos
        print(f'Versión: {version}, Longitud del Encabezado IP: {longitud_iph}, TTL: {ttl}, Protocolo: {protocolo}, Dirección de Origen: {dir_origen}, Dirección de Destino: {dir_destino}')

# Crea un socket en crudo y comienza a espiar
s = crear_socket()
espiar(s)