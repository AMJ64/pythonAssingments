#Write a function that takes a dictionary of subjects and their grades and returns the average grade. Print the result.
J = {"Maths" : 10000, "Python" : 100000, "Art" : 10000000, "Music" : 10000000000000}
l = []
sum = 0
for i,j in J.items():
    l.append((i,j))
print(l)

for k in range(0,len(l)):
    sum += int(l[k][1])
print(len(l))
d = sum/len(l)
print(d)