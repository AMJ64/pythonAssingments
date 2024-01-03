a = ["apple","banana","apple","cherry","banana","mango","mango"]
b = set({})
#count = 0
for i in range(len(a)):
    count = 0
    for j in range(0,len(a)):
        if a[i] == a[j]:
            count+=1
    b.add((a[i],count))
    #print(f"{a[i]} : {count}")

print(b)

