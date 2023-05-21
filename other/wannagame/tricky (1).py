# the task is simple.
# find a pair (a,b) which a + b = n (n is given). in all pairs, find one that LCM(a,b) is as minimum as possible.
# Example:
# n = 9 then a = 3, b = 6 (as LCM(3,6) = 6, which is the minimum in all pairs)
# n = 5 then a = 1, b = 4
# because there will be multiples answer, so we only take LCM(a,b) as the answer for the problem
from random import randint
import math
flag = b"CTF{fake_flag}"
def generate_test():
    test = []
    for i in range(20):
        test.append(randint(1, 10000000000))
    
    return test #yes, test generating is kinda bored you know

def solution(n):
    i=2
    check=1
    element = n
    while (i*i<=element):
        if(element*i==0):
            a=element//i
            b=element-a
            check=0
            break
        i+=1
    if check:
        a,b=1,element-1
    return (a*b)//math.gcd(a,b)
def xor(a,b):
    return bytes([i^j for i,j in zip(a,b)])
def solve(test):
    ans = []
    for i in test:
        ans.append(solution(i))
    
    return ans
from hashlib import sha512
from Crypto.Util.number import long_to_bytes

flag_enc_ans="cde03bc496baaf4e41f558ab275f11f521b6a9b2a576bee46be1aa9ecf631c80a6a5cfd12695d673bc6d"
flag_enc_ans= bytes.fromhex(flag_enc_ans)
test = [2242575930, 6405202397, 8061260028, 5838751172, 9141139641, 3498560665, 8439458283, 6870118638, 9538956703, 9506173776, 3094107406, 9413105427, 1344731074, 1377343799, 1605322063, 6172682165, 2358024234, 5288640112, 1869329183, 636164321]
ans = solve(test)

key = b"".join(long_to_bytes(i) for i in ans)
keyhash = sha512(key).digest()
print(keyhash)
#flag_enc = xor(flag, keyhash)
flag = xor(flag_enc_ans,keyhash)
print(flag)
# print("flag:", flag)
# print("answer:", ans)
print(flag.decode())
# print("test:", test)
# print("flag encrypted in hex:", flag_enc.hex())

# test: 
# flag encrypted in hex: cde03bc496baaf4e41f558ab275f11f521b6a9b2a576bee46be1aa9ecf631c80a6a5cfd12695d673bc6d