# n = int(input("Enter the number: "))
# rev = 0
# temp = n
# d = 0
# while n>0:
#     d = n%10
#     rev = rev * 10 + d
#     n//=10

# print(rev)

# if rev == temp:
#     print("this is a pallindrome ")
# else:
#     print("This is not a pallindrome ") 

from calendar import c


# n = input("Enter the number: " )
 
# i = 0
# j = len(n) - 1
# check = True
# while i<j:
#     if n[i] != n[j]:
#         check = False
#         break
#     i += 1
#     j -= 1
# if check == True:
#     print("This is pallindrome")

# else:
#     print("This is not pallindrome")

s = input("Enter the number: ")
i = 0
a = []
j = len(s)
while j>0:
    i+=1
    j-=1
    a.append(s[j])
y = str.join(a)
print(y)
