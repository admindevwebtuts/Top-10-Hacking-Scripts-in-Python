import socket


target = 'localhost'
port = 80
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set a timeout
s.settimeout(5)

def port_scanner(port):
    if s.connect_ex((target, port)):
        print("The port is closed")
    else:
        print("The port is open")

# Scan the first 1024 ports
for port in range(0,1025):
    print(port)
    port_scanner(port)


port_scanner(port)