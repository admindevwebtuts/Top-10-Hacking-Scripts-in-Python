import socket
import struct
import textwrap

def format_data(data):
    return '\n'.join(row for row in textwrap.wrap(data, width=80))

def unpack_packet(packet):
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);
    print('Paquete IP -> Versión:' + str(version) + ', Longitud de Encabezado:' + str(ihl) + ', TTL:' + str(ttl) + ', Protocolo:' + str(protocol) + ', Dirección de Origen:' + str(s_addr) + ', Dirección de Destino:' + str(d_addr))
    data = packet[iph_length:]
    print('Datos : ' + format_data(data.decode(errors='ignore')))

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind(("localhost", 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        raw_data, addr = s.recvfrom(65565)
        unpack_packet(raw_data)
except KeyboardInterrupt:
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    print("\nCaptura de paquetes detenida.")