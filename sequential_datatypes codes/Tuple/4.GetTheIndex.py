#Given a tuple of numbers, extract a subset from index 2 to 5. Print the result.

n = (11,23,35,46,54,67,7,8)
l = []

for i in range(len(n)):
    if 2<=i and 5 >= i:
        l.append(n[i])

print(l)