import tlv8
f=open('flag.tlv',"rb")
line = f.readline()
print(line)

print(tlv8.format_string(tlv8.deep_decode(line)))
exit()
f=f.replace('^A^D','i')
f=f.replace('^H^B','c')
f=f.replace('^S^E','t')
f=f.replace('^D^A','f')
print(f)
result=ord(f[0])
print(result)
for i in f[1:8]:
    result^=ord(i)
    print(result)
print(result)