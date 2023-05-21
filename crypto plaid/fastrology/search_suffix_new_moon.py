import hashlib
import random
import string
from multiprocessing import Process, Queue

# target hash
target_hash = "1a3021363149e766cd8aefc13165098d"

# function to generate random strings
def generate_string():
    s = ''.join(random.choice("♈♉♊♋♌♍♎♏♐♑♒♓⛎") for i in range(128))
    return s

# function to check if a string matches the target hash
def check_string(q):
    while True:
        # generate a new string
        s = generate_string()
        # hash the string
        hash_object = hashlib.md5(s.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        # check if the hash matches the target
        if hex_dig == target_hash:
            q.put(s)
            break

# number of processes
num_processes = 3

# create a queue for storing the found strings
q = Queue()

# create and start the processes
processes = []
for i in range(num_processes):
    p = Process(target=check_string, args=(q,))
    processes.append(p)
    p.start()

# wait for all processes to finish
for p in processes:
    p.join()

# get the result from the queue (this will block until a result is available)
result = q.get()

print("Found string: {}".format(result))
