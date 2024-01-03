list = [1,2,3,4,5]
r = 2
o = []
for i in range(len(list)):
    new = (i-r)%len(list)
    o.append(list[new])
print(o)


for i in range(2):
    le = list.pop()
    list.insert(0, le)
print(list)
