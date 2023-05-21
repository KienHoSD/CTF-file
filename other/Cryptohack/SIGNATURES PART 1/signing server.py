from pwn import remote # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13374, level='debug')
msg = {'option': 'get_pubkey'}
json_msg = json.dumps(msg)
r.sendline(json_msg) 

