#Write a function that takes a list of numbers as input and returns the sum of the squares of each number.

n = [1,2,3,4,5,6]
sum = 0
for i in n:
    pro = 1
    pro = i**2
    sum += pro
print(sum)
