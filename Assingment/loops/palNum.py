n = int(input("enter the value "))
digit = len(str(n))
t1 = n 
sum = 0 
pro = 0 
while(t1>0):
    pow = 1     
    for i in range(1, digit):
        x = t1%10 
        pro = x * pow
        pow = pow*10    
        t1//=10
    sum+=pro
print(sum)
if n == sum:
    print("this number is pallindrome")
else:
    print("This is not a pallindrome ")