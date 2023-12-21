s = input("enter the string to check if pallindrome or not ")
i = 0
a = []
print(s[i])
j = len(s)
check = True
while j>0:
#    if s[i] != s[j]:
#        check = False
    i+=1
    j-=1
    a.append(s[j])
print(a)
print
if check == True:
    print("this is a pallindrome string")
else:
    print("this is not a pallindrome string ")
