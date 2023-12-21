# #another way to reverse a string 
# n = input("enter the number: ")
# pal = n
# last_index = len(pal) - 1
# a = []
# b = []

# for i in range(0,last_index+1):
#     b.append(n[i])


# for j in range(last_index,-1,-1):
#     a.append(n[j])
# print(a)


# if b == a:
#     print("the is a pallindrome ")
# else:
#     print("this is not a pallindrome")

#Write a program to check if the given string is pallindrome or not

# name = "malayalam"
# rev_name = name[::-1]
# if name == rev_name:
#     print("This string is pallindrome")
# else:
#     print("this is not a pallindrome ")


n = "malayalam"

i = 0
j = len(n)-1
c = 0
while i<j:
    if n[i] != n[j]:
        c = 1
    i+=1
    j-=1

if c == 0:
    print("this is a pallindrome ")
else:
    print("This is not a pallindrome ") 

    

    



