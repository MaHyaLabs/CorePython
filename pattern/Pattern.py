def printhello():
    print("HelloMahya")


def pattern1():
    for x in range(1, 6):
        for y in range(1, 6):
            print("*", end="")
        print()


def pattern2():
    for x in range(1, 6):
        for y in range(1, 6):
            print(y, end="")
        print()


def pattern3():
    for x in range(5, 0, -1):
        for y in range(5, 0, -1):
            print(x, end="")
        print()


def pattern4():
    n=5;
    k=1;
    for x in range(1, n+1):
        for y in range(1, n+1):
            print("{:2d} ".format(k), end="")
            k +=1
        print()


class Pattern:
    printhello()
    pattern4()
