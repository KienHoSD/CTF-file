import hashlib
import random
import string

def generate_string():
    prefix = 'O9D8nbsf82'
    s = prefix + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
    return s

while True:
    s = generate_string()
    if hashlib.sha256(s.encode('ascii')).hexdigest()[-6:] == "ffffff":
        print("Found string: {}".format(s))
        break