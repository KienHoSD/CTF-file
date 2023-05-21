import time
import random
import socket

host = '134.122.101.249'
port=32415
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host,port))
seed = int(time.time())
random.seed(seed)
ansnumbers=[]
while len(ansnumbers) < 10:
    r = random.randint(1, 90)
    if(r not in ansnumbers):
        ansnumbers.append(r)
print(ansnumbers)
for _ in range(12):
    received_data = client_socket.recv(1024).decode()
    print(received_data)
ans=''
for i in ansnumbers[5:10]:
    ans+=str(i)+' '
print(ans)
client_socket.sendall(ans.encode())
print(client_socket.recv(1024).decode())

