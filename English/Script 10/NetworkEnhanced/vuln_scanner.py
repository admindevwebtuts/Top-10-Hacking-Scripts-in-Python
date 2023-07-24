import socket
import threading

# Define a function to scan a single port
def scan(target_ip, port, lock):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, port))
        lock.acquire()   # Acquire the lock before printing
        print(f'Port {port} is open.')
        lock.release()   # Release the lock after printing
        sock.close()
    except:
        pass

# Create a lock object
lock = threading.Lock()

# Scan ports from 1 to 1024
for port in range(1, 1024):
    thread = threading.Thread(target=scan, args=('127.0.0.1', port, lock))
    thread.start()
