'''
153 = 1^3 + 5^3 + 3^3
153 = 1 + 125 + 27

371 = 3^3 + 7^3 + 1^3
371 = 27 + 343 + 1

370 = 3^3 + 7^3 + 0
370 = 27 + 343

1634 = 1 + 216 + 27 + 64
1634 = 1 + 1296 + 81 + 256  = 1634

'''

n = int(input("enter the number  "))
sum = 0
temp = n
while(n>0):
	dig = n%10
	sum = sum + dig**3
	n = n//10
if temp == sum:
	print("this is an armstrong number")
else:
	print("This is not an armstrong number")
	