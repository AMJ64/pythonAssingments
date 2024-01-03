n = [1,2,3,4,5,6,7,8,9,10]
count = 1
for i in range(1,n.__len__()-1):
    count = count + n[i]
    print(n[i])

print(count)