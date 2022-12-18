def writetoFile():
    a = 10
    b = 15
    st="Hello Mahya this is function op"
    return st


f = open("sample1.txt", "a")
f.write(str(writetoFile()))
f.close()
f = open("sample1.txt", "r")
print(f.read())
f.close()

