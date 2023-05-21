

from Crypto.Util.number import bytes_to_long, getPrime,inverse,long_to_bytes
from gmpy2 import iroot
with open(r"C:\Users\chann\Desktop\CTF file\Cryptohack\output.txt") as f:
    lines = f.readlines()
n=[]
for i,text in enumerate(lines):
    if i%5==0:
        n.append(int(text[4:].replace("\n","")))
c=[]
for i,text in enumerate(lines):
    if (i%5)-2==0:
        c.append(int(text[4:].replace("\n","")))

def broadcast_attack(data):
    def extended_gcd(a,b):
        x, y = 0, 1
        lastx, lasty= 1, 0
        while b:
            a , (q,b) = b, divmod(a,b)
            x , lastx = lastx - q *x, x
            y , lasty = lasty - q *y, y
        return (lastx,lasty,a)
    def chinese_remainder_theorem(items):
        M=1
        for a,m in items:
            M*=m
        result = 0
        for a,m in items:
            M1=M//m
            r,s,d = extended_gcd(m,M1)
            if d != 1:
                M=M//m
                continue
            result+=a*M1*s
        return result%M
    m= chinese_remainder_theorem(data)
    m= iroot(m,3)[0]
    return m



for i in range(5):
    for j in range(i + 1, 6):
        for k in range(j + 1, 7):
            data = [(c[i], n[i]), (c[j], n[j]), (c[k], n[k])]
            m = long_to_bytes(broadcast_attack(data))
            if b'crypto{' in m:
                print(i, j, k, )
                print(m.decode())
exit()
for i in range(0,5):
    for j in range(i+1,6):
        for e in range(j+1,7):
            data= [(n[i],c[i]),(n[j],c[j]),(n[e],c[e])]
            flag = long_to_bytes(broadcast_attack(data))
            if b'crypto{' in flag:
                print(flag.decode())
#print(data[0])
#print(broadcast_attack(data))

exit()

def RSA_encrypt(message):
    m = bytes_to_long(message)
    p = getPrime(1024)
    q = getPrime(1024)
    N = p * q
    e = 3
    c = pow(m, e, N)
    return N, e, c


for m in messages:
    N, e, c = RSA_encrypt(m)
    print(f"n = {N}")
    print(f"e = {e}")
    print(f"c = {c}")
