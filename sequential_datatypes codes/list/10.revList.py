#Reverse the order of elements in a given list of characters. Print the reversed list.

n = ["a" , "b" ,"a" , "c" , "b", "d"]

for i in range(len(n)-1, -1, -1):
    print(n[i])
