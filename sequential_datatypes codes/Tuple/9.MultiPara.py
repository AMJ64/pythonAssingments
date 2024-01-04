#Write a function that takes multiple parameters and returns them as a tuple

l = []
for i in range(0,5):
    for j in range(4,-1,-1):
    #     x = int(input("enter the x coordinate "))
    #     y = int(input("enter the y coordinate "))
        l.append((i,j))
print(l) 