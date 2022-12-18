def numberisevenodd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


def fact():
    facto = 1;
    n = int(input("enter the number:"))

    for i in range(1, n + 1):
        print(i)
    # facto = facto*i
    # print("factorial of ", n ,"is ",facto)


def ifelsecheck():
    if 5 > 2:
        print("first iss great")
    else:
        print("second is great")


class Number:
    # num=int(input("Enter number"))
    # numberisevenodd(num)
    # fact()
    ifelsecheck()
    ab = "mahesh"
    c= "sd"
    print(ab[3]+c[1])
