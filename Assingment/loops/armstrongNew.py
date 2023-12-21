n = int(input("enter the number to check "))

# while(t1>0):
#     t1//=10
#     dig+=1
# print(dig)

dig = len(str(n))

t2 = n
sum = 0
while(t2>0):
    d = t2%10
    sum = sum + d**dig
    t2 //= 10
if n == sum:
    print("this is a armstrong")
else:
    print("this is not a armstrong")