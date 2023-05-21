from Crypto.Cipher import ChaCha20
import os
from pwn import xor
f =open("out.txt","rb")
iv = f.readline()
ms= f.readline().strip()
flag = f.readline().strip()
message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"
flag= xor(ms,flag)
print(flag)
result = xor(flag,message)
print(result.decode())
exit()
def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def Writedata(data):
    with open("outtest.txt", "w+") as f:
        f.write(data)

if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"
    key, iv = os.urandom(32), os.urandom(12)
    print(key,iv)
    encrypted_message = encryptMessage(message, key, iv)
    encrypted_flag = encryptMessage(FLAG, key, iv)

    data = iv.hex() + "\n" + encrypted_message.hex() + "\n" + encrypted_flag.hex()
    
    Writedata(data)