import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP server listening on port {UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")
