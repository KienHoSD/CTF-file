
from random import randint
from Crypto.Util.number import getPrime
def xor(a,b):
    return bytes([i^j for i,j in zip(a,b)])

from hashlib import sha256
from Crypto.Util.number import long_to_bytes

def challenge(): # if u have super computer, maybe you can bruteforce it
    key = []
    sum = 0
    pubkey = []
    for i in range(40):
        a = randint(1, 1000000000000000000)
        if randint(0,1):
            key.append(a)
            sum += a
        pubkey.append(a)
    
    
    keyhash = sha256(b"".join(long_to_bytes(i) for i in key)).digest()
    flag_enc = xor(flag, keyhash)
    return key,sum, pubkey, flag_enc


key ,sum, pubkey, flag_enc  = challenge()

print("hint:", sum)
print("pubkey:", pubkey)
print("flag encrypted in hex:", flag_enc.hex())

# hint: 7394434369910335785
# pubkey: [372095569253122159, 980546934628891627, 396420740362603163, 29547817979441939, 957963034591483508, 788394514740094577, 874502675584381327, 498889291874387902, 639325703534670353, 465296604822943367, 652585066666217802, 383116152788059160, 329740728497538212, 378284568716532708, 308136957796662942, 854528376834365280, 405760121428415580, 572353331045961500, 487384402954222, 587973628703958489, 967394744991781950, 991116164172481186, 688342924722299534, 558868906136672515, 372322267735121185, 818222118510751892, 921823835285223664, 505712538217401656, 162997687889187245, 992794340338652972, 641885996859593436, 405962455028813769, 283474956206677683, 732187224082874960, 913332629601773362, 464887333416442922, 572428042374711359, 465900707733032664, 584827825896317680, 249695854246092754]
# flag encrypted in hex: 3b3d6e12561045084651b0130b492694192cabdd15f8a650af7601

