#we all know trianlge have 3 sides that is why we are going to take 3 parameteres 

n = int(input("side a "))
c = int(input("side b "))
a = int(input("side c "))

if n==a and n==c:
    print('equilateral triange')
elif n!=a and n!=c and a!=c:
    print('Scalene triangle')
elif n==a and n!=c:
    print('isoceles triangle')
elif n==c and n!=a:
    print('isoceles triangle')