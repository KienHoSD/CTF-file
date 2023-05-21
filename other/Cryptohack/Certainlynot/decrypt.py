from Crypto.PublicKey import RSA

f = open(r"C:\Users\chann\Desktop\CTF file\Cryptohack\Certainlynot\certificate.pem","r")
key = f.read()
enc = RSA.importKey(key)
print(enc.n)
