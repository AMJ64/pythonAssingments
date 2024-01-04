#Create two tuples representing colors and concatenate them. Print the resulting combined tuple.

n = ("orange", "red","white", "black")
m = ("blue", "yellow","green")

x, y  = list(n),list(m)
c = x + y

n = tuple(c)
print(type(n))
print(n)