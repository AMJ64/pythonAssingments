#0 1 1 2 3 5 8 13 21 34 55 
x = 0
y = 1
print(x)
print(y)
for i in range(0,20):
    x, y = y, x + y
    print(y)
