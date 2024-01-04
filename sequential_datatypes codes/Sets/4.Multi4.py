#Given a set of even numbers, filter out the multiples of 4. Print the modified set.
s = set({})
for i in range(0,20,2):
    if i%4 == 0:
        s.add(i)
print(s)
    



    
