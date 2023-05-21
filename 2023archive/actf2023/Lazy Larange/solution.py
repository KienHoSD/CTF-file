import random
import socket

HOST = 'challs.actf.co'
PORT = 32100

with open('flag.txt', 'r') as f:
    FLAG = f.read()

assert all(c.isascii() and c.isprintable() for c in FLAG), 'Malformed flag'
N = len(FLAG)
assert N <= 18, 'I\'m too lazy to store a flag that long.'
p = None
a = None
M = (1 << 127) - 1

def query1(s):
    if len(s) > 100:
        return 'I\'m too lazy to read a query that long.'
    x = s.split()
    if len(x) > 10:
        return 'I\'m too lazy to process that many inputs.'
    if any(not x_i.isdecimal() for x_i in x):
        return 'I\'m too lazy to decipher strange inputs.'
    x = (int(x_i) for x_i in x)
    global p, a
    p = random.sample(range(N), k=N)
    a = [ord(FLAG[p[i]]) for i in range(N)]
    res = ''
    for x_i in x:
        res += f'{sum(a[j] * x_i ** j for j in range(N)) % M}\n'
    return res

def query2(s):
    if len(s) > 100:
        return 'I\'m too lazy to read a query that long.'
    x = s.split()
    if any(not x_i.isdecimal() for x_i in x):
        return 'I\'m too lazy to decipher strange inputs.'
    x = [int(x_i) for x_i in x]
    while len(x) < N:
        x.append(0)
    z = 1
    for i in range(N):
        z *= not x[i] - a[i]
    return ' '.join(str(p_i * z) for p_i in p)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        if '1. Evaluate a polynomial' in data:
            s.sendall(b'1\n')
            x = random.randint(0, 10**9)
            s.sendall(f'{x}\n'.encode())
            res = s.recv(1024).decode()
            print(res.strip())
        elif '2. Recover the flag' in data:
            s.sendall(b'2\n')
            res = s.recv(1024).decode()
            print(res.strip())
            flag = res.strip().split()
            assert len(flag) == N
            flag = [int(flag[i]) for i in range(N)]
            flag = ''.join(chr(flag[i]) for i in range(N))
            print(f'The flag is: {flag}')
            break
