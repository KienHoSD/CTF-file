from Crypto.Util.number import long_to_bytes as ltb,inverse
from math import gcd
e=0x10001
f=open("output.txt","r")
n1 = int(f.readline()[3:])
c1 = int(f.readline()[3:])
c2 = int(f.readline()[3:])
H = int(f.readline()[14:])
n2 = H%n1
q = gcd(n1,n2)
p = n1//q
z = n2//q
phi1 = (q-1)*(p-1)
phi2 = (q-1)*(z-1)

d1= inverse(e,phi1)
d2= inverse(e,phi2)

flag= ltb(pow(c1,d1,n1)) + ltb(pow(c2,d2,n2))
print(flag.decode())
