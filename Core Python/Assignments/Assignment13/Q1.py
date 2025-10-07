# Python Program to Add a Key-Value Pair to the Dictionary

n = int(input("Enter size of dictionary: "))
dict = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = input("Enter the value: ")
    dict[key] = value       ## to add key-value pair in the empty dictionary(dict = {})

print(dict)