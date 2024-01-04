#Sort a tuple of strings in reverse alphabetical order. Print the result.

t = ("Python", "Java", "C++", "R", "Php" , "JS")
l = list(t)
l.sort()
l.reverse()
print(tuple(l))
