n = int(input("enter the number "))

#count the number of digits
sum = 0
dig = 0
t1 = n
while(t1>0):
    t1//=10
    dig += 1

#products of the armstrong number 
t2 = n
rem = 0
while(t2>0):
    rem = t2%10
    pro = 1
    for i in range(1,dig+1):
        pro*=rem
#add the products
    sum = sum + pro
    t2//=10

print("This is the addition of the number after raised power: ",sum)

#compare the sum to the original number 
if sum == n:
    print("This is an armstorng Number ")
else:
    print("This is not an Armstrong Number")


    

