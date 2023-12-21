#print even number from 1 to 100 
#print armstrong number from 100 to 10000
for i in range(100,10001):
    n = i
    rem = 0
    sum = 0
    digit = len(str(n))
    t1 = n
    while(t1>0):
        rem = t1%10
        pow = 1
        for i in range(1, digit+1):
            pow = pow * rem
        sum+=pow
        t1 //= 10
    if n == sum:
        print(n)

