import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 15101 #Debe ser el mismo que se configuró en el ESP_ModemFO

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(4096)
    print("received message:", data)
