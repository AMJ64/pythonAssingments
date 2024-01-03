l = [1,2,3,4,5,6,7,8]
s = 3
res = []
temp = []

for i in l:
    temp.append(i)
    if len(temp) == s:
        res.append(temp)
        temp = []
print(temp)
if temp:
    res.append(temp)

print(res)