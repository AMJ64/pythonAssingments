fruits = ["apple", "banana", "apple", "cherry", "banana","mango","mango","mango"]
counter = {}

for i in fruits:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
        print(counter)
print(counter)
# for fruit, count in counter.items():
#     print(f"{i}: {count}")
