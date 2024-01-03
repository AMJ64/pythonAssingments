L = [1,1,2,2,2,3,3,3,3]
M = []
for i in L:
    if i not in M:
        M.append(i)
print(M)