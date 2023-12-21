n = int(input("enter First number  "))
m = int(input("enter Second number "))
a = int(input("enter Third number "))

if n>m:
    if n>a:
        print("First number is Greatest")

if m>n:
    if m>a:
        print("Second Number is Greatest")
        
if a>m:
    if a>n:
        print('Third number is Greatest')
