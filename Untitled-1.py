#sum = 0
#for i in range(34,79):
#    if(i%2==0):
#        sum += 1
#print(sum)
#write a program if a number is a prime number 
#write a program is a number is an amstrong number 


#sum = 0
count = 0
pruduct  = 1
'''for i in range(1,101):
    num = i
    chk = True
    for i in range(2,num):
        if (num % i == 0):
            chk = False
            break;
    if chk == True:
        sum = sum + num
print(sum)
'''#15

#amstrong number

'''
tum = 0
n = int(input("Enter the number"))
temp = n
c = len(n)
while n>0:
    for i in range(1,c+1):        
        temp = temp//10
        sum = sum**3

    
if tum == n :
    print ("Amstrong Number")
else:
    print ("Not Amstrong Number")
'''

for i in range(1,1001):
    temp = i
    sum = 0
    while i>0:
        digit = i%10
        sum  = digit**3+sum
        i = i//10
    if temp == sum:
        print(sum)


