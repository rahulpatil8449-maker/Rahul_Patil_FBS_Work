# Python Program to Multiply All the Items in a Dictionary

n = int(input("Enter size of dictionary: "))
dict = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = int(input("Enter the value: "))
    dict[key] = value       ## to add key-value pair in the empty dictionary(dict = {})

print("Original Dictionary is:", dict)

total = 1

for key in dict:
    total *= dict[key]

print("The Sum of all items in the dictionary will be:", total)