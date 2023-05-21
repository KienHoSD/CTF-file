from string import printable
f = open("msg.enc","r")
line = f.readline()
# print(line)
ct = bytes.fromhex(line)
# print(ct)
for i in ct:
    for j in printable:
        if (123 * ord(j) + 18) % 256 == i:
            print(j,end = '')

