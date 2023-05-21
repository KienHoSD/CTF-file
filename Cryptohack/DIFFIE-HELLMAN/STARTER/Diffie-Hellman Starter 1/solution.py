p = 991
g = 209
#find the inverse element d such that g * d mod 991 = 1.
from Crypto.Util.number import inverse
d = inverse(g,p)
print(d)