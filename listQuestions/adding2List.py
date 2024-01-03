n = int(input("enter the number "))
a = []
b = []
for i in range(0,n):
    x = int(input("enter the number: "))
    a.append(x)

print(f"This is the first list{a}")

for j in range(0,n):
    y = int(input("enter the number: "))
    b.append(j)
print(f"These are the first and second lists{a} and {b}")

L = a + b
o = len(L)-1
for i in range(o):
    for j in range(0,o-i-1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

print(L)