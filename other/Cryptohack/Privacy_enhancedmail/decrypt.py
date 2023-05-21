from Crypto.PublicKey import RSA

f = open(r"C:\Users\chann\Desktop\CTF file\Cryptohack\Privacy_enhancedmail\privacy_enhanced_mail.pem", "r")
key = f.read()
enc = RSA.importKey(key)
print(enc.d)
