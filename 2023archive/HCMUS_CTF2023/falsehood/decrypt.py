import os
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import random
import ast
import itertools
import binascii
from sage.all_cmdline import *
f = open("output.txt","r")
e = ast.literal_eval(f.readline())
matrix_left=[]
matrixtemp=[]
for i in range(16):
    matrixtemp=[]
    for j in range(16):
        matrixtemp.append(e[i][0]**j)
    matrix_left.append(matrixtemp)

matrixans=[]
for i in range(16):
    matrixans.append([e[i][1]])
matrix_left = matrix(matrix_left)
matrixans = matrix(matrixans)
# solve linear algebra
key = matrix_left.solve_right(matrixans)
# making sage matrix to list in python
key = key.list()
# print(key)
key = b''.join([int(i).to_bytes(1, 'big') for i in key])
ct="be205fd34ebe59af55ea11fec9aea50197fbf35d5b52c650a6c9563186625e8b6021ba31db538fa4b60c69a42c96ee3bebaba53ac9afa9c3c185d4d0b145bc8251d892c243f1aa4037aeea003714e24c"
iv='370abc6fce33f812de7b88daaa82e4c4'
ct=bytes.fromhex(ct)
cip = AES.new(key, AES.MODE_CBC,bytes.fromhex(iv))
flag = unpad(cip.decrypt(ct),16)
print(flag.decode())


            




