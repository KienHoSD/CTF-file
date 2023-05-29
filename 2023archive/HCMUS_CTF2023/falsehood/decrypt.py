import os
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import ast
import itertools
import binascii
bool_array = [True, False]

# Iterate over all possible combinations of True and False

f = open("output.txt","r")

e = ast.literal_eval(f.readline())

matrix = []
matrix2=[]
for i in range(16):
    matrix2=[]
    for j in range(16):
        matrix2.append(e[i][0]**j)
    matrix.append(matrix2)


matrixans=[]
for i in range(16):
    matrixans.append([e[i][1]])
        
X=[151, 31, 144, 9, 171, 106, 24, 3, 175, 203, 78, 154, 44, 113, 201, 46] 
key = b''.join([int(i).to_bytes(1, 'big') for i in X])
ct="be205fd34ebe59af55ea11fec9aea50197fbf35d5b52c650a6c9563186625e8b6021ba31db538fa4b60c69a42c96ee3bebaba53ac9afa9c3c185d4d0b145bc8251d892c243f1aa4037aeea003714e24c"
iv='370abc6fce33f812de7b88daaa82e4c4'
ct=bytes.fromhex(ct)
cip = AES.new(key, AES.MODE_CBC,bytes.fromhex(iv))
flag = cip.decrypt(pad(ct,16))
print(flag)


            




