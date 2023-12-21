num = int(input("enter number to check pallindrome "))
dig = len(str(num))

t1 = num
s = 0
while t1>0:
    d = t1%10
    s = s + d ** dig
    t1//=10

print(f"the sum of the products after loop execution {s}")
if num == s:
    print("armstrong number ")
else:
    print("not armstrong number")