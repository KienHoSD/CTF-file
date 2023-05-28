import socket
import json
ip_address = "calc-1.ctf.hackaplaneten.se" #ip host
port = 1337 #port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))
received_data = client_socket.recv(1024).decode()
received_data = client_socket.recv(1024).decode()
print("Received:", received_data)

client_socket.sendall('2 + 2'.encode())
received_data = client_socket.recv(1024).decode()

print("Received:", received_data)
exit()
for i in range(32):
    f = e.recv().decode()
    print(f)
    e.send(("2 + 2").encode())
