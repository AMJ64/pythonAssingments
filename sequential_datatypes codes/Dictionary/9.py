#Sort a dictionary by values in ascending order. Print the sorted dictionary.

d = {"apple": "Fal he" , "La Ferrari ": "Car he ", "Sarangheo" : "Song he", "Nichijou" : "Japanai Cartoon"}
l = []
for i,j in d.items():
    l.append((i,j))
l.sort()
print(l)