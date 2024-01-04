#list comprehension
# num = [i for i in range(10,0,-1) if (i%2==0)]
# print(num)

# letters = [letter.upper() for letter in "abcdefghijklmnopqrstvvwxyz"] [:8]
# print(letters)

# lo = [wo for wo in ["Short" ,"Medium", "Long", "damudamudamudamu"] if len(wo)>5]
# print(lo)

# g = [(x,y) for x in range(-5,6) for y in range(-5,6)]
# print(g)

# num = [2,3,4,5,6,7]
# tran = [x**2 if x%2 == 0 else 2*x for x in num]
# print(tran)

#Slicing and Dicing 
# num = "Python is a language"
# x = num[6::-1]
# y = num[12:len(num)]
# z = num[:6]
# w = num[6:len(num)]
# print(x)
# print(y)
# print(z)
# print(w)
# #start stop skip

x = {"apple":"a fruit ", "tomato": "a vegetable"}
y = {"kung fu" : "is a movie", "ferrari" : "is a car"}
z = []
# m = list(x)
# m.append((y.keys(),y.values()))

# print(m)

for i,j in x.items():
    z.append((i,j))
for l,m in y.items():
    z.append((l,m))

    
print(dict(z))
z = x.copy(),y.copy()
print(dict(z))
