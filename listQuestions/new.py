n = [1,2,3,4,5]
first = n[0]
rotate = 2
for i in range(0,len(n)):
    n[0]= n[len(n)-1]
    for j in range(1,len(n)-1):
        n[i] = n [j]

n[rotate] = first

print(n)
