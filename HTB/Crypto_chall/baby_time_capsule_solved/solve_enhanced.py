from Crypto.Util.number import long_to_bytes
from attacks.rsa.hastad_attack import attack
import socket
import json
ip_address = "144.126.192.42" #ip host
port = 30685 #port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))
ct=[]
n=[]
for _ in range(5):  
    received_data = client_socket.recv(1024).decode()
    print("Received:", received_data)
    senddata = "y"
    client_socket.sendall(senddata.encode())
    received_data = client_socket.recv(1024).decode()
    print(received_data)
    revdata = json.loads(r"{}".format(received_data))
    ct.append(int(revdata["time_capsule"],16))
    n.append(int(revdata["pubkey"][0],16))
# print(ct)
e=5
print(long_to_bytes(attack(n,e,ct)).decode())