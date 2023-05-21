for i in range(1,8):
    f= open("input-{}.txt".format(i), "r")
    file = open("answer{}.txt".format(i), "w")
    arr= []
    numberofnumber = int(f.readline())
    arr = f.readline().split()
    for i in arr:
        file.write(str(abs(int(i)))+" ")