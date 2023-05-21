from Crypto.Util.number import getPrime, long_to_bytes, inverse,bytes_to_long
from gmpy2 import iroot
f=open("output.txt","r").readline()[6:]
ct = bytes.fromhex(f)
print(long_to_bytes(iroot(bytes_to_long(ct),3)[0]))


