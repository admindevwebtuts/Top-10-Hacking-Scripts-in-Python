# vuln_scanner.py

# Importing necessary libraries
import socket

# Defining the scanning function
def scan(target_ip):
    for port in range(1, 1024):   # We scan the first 1023 ports as they are well-known ports
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            sock.settimeout(1)   # We set a timeout for the connection attempt
            sock.connect((target_ip, port))   # We attempt to connect to the target IP on the current port
            print(f'Port {port} is open.')
            sock.close()
        except:
            print(f'Port {port} is close.')
            pass

# Running the scanner on localhost
scan('127.0.0.1')
