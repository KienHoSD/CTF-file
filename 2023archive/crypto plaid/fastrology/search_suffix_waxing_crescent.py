import hashlib
import random
import string
import threading

# target hash
target_hash = "a1dd73d0af2539541d84aee4e3c1bcc3"

# function to generate random strings
def generate_string():
    s = ''.join(random.choice("☊☋☌☍") for i in range(128))
    return s

s= generate_string()
print(s)
print(hashlib.md5(s.encode('utf-8')).hexdigest())
exit()
# function to check if a string matches the target hash
def check_string():
    while True:
        # generate a new string
        s = generate_string()
        # hash the string
        hash_object = hashlib.md5(s.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        # check if the hash matches the target
        if hex_dig == target_hash:
            print("Found string: {}".format(s))
            break

# number of threads
num_threads = 10

# create and start the threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=check_string)
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()