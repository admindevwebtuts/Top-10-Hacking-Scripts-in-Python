import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind(("localhost", 0))

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        print(s.recvfrom(65565))
except KeyboardInterrupt:
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    print("\nLa detección de paquetes se detuvo.")