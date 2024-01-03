a = [1,2,3,4,5,6,7,8,9]
n = int(input("enter the number to get it's index: "))


if n in a:
    print("Index of ",n,":",a.index(n))
else:
    print(-1)