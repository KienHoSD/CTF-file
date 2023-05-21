import os
from pwn import xor
f = open("output.txt","r")
ct = bytes.fromhex(f.readline()[6:])
key = xor(ct[:4],b'HTB{')
flag = xor(ct,key)
print(flag.decode())
