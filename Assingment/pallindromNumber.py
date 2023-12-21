num = int(input("Enter the number "))
for i in range(0,num):
    temp = i
    rev = 0

    while i>0:
        dig = i%10
        rev = rev*10 + dig
        i = i//10

    if rev == temp:
        print(f'this is a pallindrome number {temp}')
   

