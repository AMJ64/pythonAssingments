#n = input("enter number string float or boolian ")
n = 'wasd'
x = type(n)
y = str(x)
print(y)
match y:
    case 'str':
        print("string")
