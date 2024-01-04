#Remove a specific key-value pair from a dictionary of countries and capitals. Print the modified dictionary.
j = {"Tea": "Milk", "Sandwich":"Bread", "Ice":"Charizard"}
l = []
for i in j.items():
    l.append(i)
print(l)
l.pop()
print(dict(l))