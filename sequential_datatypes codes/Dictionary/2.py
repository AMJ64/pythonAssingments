# Creat a dictionaries respresenting contacts. Merge them and print the combined dictionary.

a = {"Leo" : 9898989898 , "Vikram" : 4984651684}
b = {"Tinku" : 7894156132, "Jiya" : 798615161}
c = []
for i,j in a.items():
    c.append((i,j))
for l,m in b.items():
    c.append((l,m))

print(dict(c))
