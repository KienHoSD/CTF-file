from sage.all import *
from random import randint
pubkey = Matrix(ZZ, [
    [47, -77, -85],
    [-49, 78, 50],
    [57, -78, 99]
])
r = open("wordlistofr.txt","r")
e = open("enc.txt","r")
rtemp=eval(r.readline())
vectorran=vector(rtemp)
for i in range(47):
    rtemp2=eval(e.readline())
    vectorran2=vector(rtemp2)
    print(chr(((vectorran2-vectorran)/pubkey)[0]),end='')
    
