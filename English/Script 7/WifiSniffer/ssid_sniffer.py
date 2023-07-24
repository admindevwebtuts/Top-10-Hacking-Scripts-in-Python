import socket
import struct
import sys

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('Socket could not be created. Error Code: ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    return s

def sniff(s):
    while True:
        packet = s.recvfrom(65565)
        packet = packet[0]
        # We'll parse the packet using struct
        ip_header = packet[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        # Print some of the info we just parsed
        print(f'Version: {version}, IP Header Length: {iph_length}, TTL: {ttl}, Protocol: {protocol}, Source Address: {s_addr}, Destination Address: {d_addr}')

# Create a raw socket and start sniffing
s = create_socket()
sniff(s)
