#Generate a set of cubes for numbers 1 to 5 using set comprehension. Print the resulting set.
cube = {x**3 for x in range(1,6)}
list(cube).sort()
print(cube)