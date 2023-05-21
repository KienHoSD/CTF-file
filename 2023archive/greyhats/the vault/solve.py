from hashlib import sha256 
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 
from math import log10 


def encryption(key, plaintext):
    iv = "Greyhats".encode()
    cipher = AES.new(key, AES.MODE_CTR, nonce = iv)
    return cipher.encrypt(plaintext)
thief_check = get_random_bytes(16)
print(thief_check)
n = pow(10, 128)
a = int(input("Enter the first code: "))
b = int(input("Enter the second code: "))
print(a,b)
for i in range(10000):
    if (i%10==0):
        continue
    for j in range(10000):
        if j * log10(i) <= 128:
            continue
        x = pow(i, j, n)
        if x == pow(x,10,n):
            print(i,j)
# x = pow(a, b, n)
# print(x, pow(x,10,n))
exit()
first_key= sha256(long_to_bytes(x)).digest()
e=encryption(first_key, encryption(first_key, thief_check))
print(e)
