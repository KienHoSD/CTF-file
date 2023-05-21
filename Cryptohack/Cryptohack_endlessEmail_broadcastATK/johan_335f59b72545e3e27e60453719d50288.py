

from Crypto.Util.number import bytes_to_long, getPrime
with open(r"C:\Users\chann\Desktop\CTF file\Cryptohack\output.txt") as f:
    lines = f.readlines()
n=[]
for i,text in enumerate(lines):
    if i%5==0:
        n.append(text[4:].replace("\n",""))
c=[]
for i,text in enumerate(lines):
    if (i%5)-2==0:
        c.append(text[4:].replace("\n",""))

print(c)


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
