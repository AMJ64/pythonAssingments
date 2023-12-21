#step 1 Here we are taking the input from the user to check 

n = int(input("enter the number "))
dig = 0

#Step 2: We are initializing a fresh variable to that our actual input stays the same till end 

t1 = n

#Step 3: We are initializing/using a while loop to count the number of digits in this given input number

while(t1>0):
    t1//=10
    dig+=1

#Step 4: Same as step 2

t2 = n

#Step 4 we are initalizing another loop so that those numbers can go one by one and get their value raised by powers 

while(t2>0):
    rem = t1%10
    product = 1

#This inner loop here performs the actual multiplication of raising the powers of the numbers 1 by 1

    for i in range(1, dig+1):
        product*=rem

#Step 5 we are now adding all the products of the single numbers to this one variable called sum

    sum +=product
    t1//=10

#Step 6 (optional): This step is just to actually check what is their addtion value after the whole program is written

print("The actual sum of the separated digits after raised to their corresponding powers \n", sum)

#Step 7: Using if-else condition to check if the number is armstrong or not

if n == sum:
    print("This is an armstrong")
else:
    print("This is not an armstrong")