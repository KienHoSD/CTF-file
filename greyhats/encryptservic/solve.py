from pwn import remote,xor
f = remote("34.124.157.94", 10590)
recv=f.recv().decode()
# print(recv)
f.sendline(b"61616161616161616161616161616161616161616161616161616161616161616161616161616161")
hex = []
for i in range(256):
    mess = f.recvline().decode()
    hex.append(mess[-81:-1])
# print(hex)
mess =f.recvall().decode()
flag = mess[-81:-1]
for i in hex:
    tempi= bytes.fromhex(i)
    tempflag = bytes.fromhex(flag)
    ans= xor(tempi,tempflag,b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    if b'grey' in ans:
        print(ans.decode())