#Convert a list of unique numbers to a set. Print the resulting set

l = [1,5,3,5,4,9,6,3,12,4,8,6,2,1,4,45,2,65,8,8,2,]
M = set({})

for i in l:
    if i not in M:
        M.add(i)
print(M)