from pwn import remote # pip install pwntools
r = remote('challs.actf.co', 31402,level = 'debug')
for stage in range(100):
    received=r.recv()
    r.sendline(received[31:34]+received[-4:-1]) 