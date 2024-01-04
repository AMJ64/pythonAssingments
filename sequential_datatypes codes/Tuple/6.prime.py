#Check if a specific element exists in a tuple of prime numbers. Print the result.
n = int(input("enter the number to check "))
l = []
for i in range(1,101):
    chk = True
    for j in range(2,i):
        if i%j == 0:
            chk = False
            break
    if chk == True:
        l.append(i)
print(l)
m = tuple(l)
if n in m:
    print(f"{n} is present in the tuple")