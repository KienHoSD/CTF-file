import sys
import os
import numpy as np
import random
import json
import string
import itertools
import math
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl, inverse
from pwn import remote, process, log, args, debug, info, log as pwnLog
from tqdm import tqdm, trange
from matplotlib import pyplot as plt
from functools import reduce, cache
from base64 import b64encode, b64decode
from collections import Counter
from attacks.factorization.coppersmith import factorize_p
from shared.partial_integer import PartialInteger

n = 137695652953436635868173236797773337408441001182675256086214756367750388214098882698624844625677992374523583895607386174643756159168603070583418054134776836804709359451133350283742854338177917816199855370966725059377660312824879861277400624102267119229693994595857701696025366109135127015217981691938713787569
leak = 6745414226866166172286907691060333580739794735754141517928503510445368134531623057
ct = 6093958566038680127326434533694328259546629713130935781737870800313530023106573401782903835801927155350835656312285112061565564002395126816287398095756072942491374865711629386081545322545370627438802718290674160593090851032972187400400078354859941446235514386892220406085066621097883723118772229549675375699
p,q =factorize_p(
    n, # modulus 
    PartialInteger.parse_be(f"{leak:0272b}" + '?'*240, 2), # f(x) = (leak * 2^240) + x
    0.5, # beta for solving equation on f(x) mod n^beta
    0.03  # decrease this for higher shift => Bigger lattice dimension => Take more computation power but more accuracy
)
print(p,q)
print(ltb(pow(ct, inverse(0x10001, (p-1)*(q-1)), n)))

