n = int(input("enter the number to check if prime or not "))
check = True

for i in range(2,n):
    if (n % i) == 0:
        check = False
        break

if check == True:
    print("This is a prime number")

if check == False:
    print("this is not a prime number")