s = input("Enter string : ")
#java
i = 0
j = len(s)-1
chk = True
while i<j:
    if s[i] != s[j]:
        chk = False
    i+=1
    j-=1

if chk == True:
    print("this is a pallindrome")
else:
    print("This is not a pallindrom string")