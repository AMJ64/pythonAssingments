x = 0
y = 1
print(x)
print(y)
for i in range(1,10):
    z = y
    y = x + y
    x = z    
    print(y)