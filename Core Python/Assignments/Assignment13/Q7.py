# Python Program to Remove the Given Key from a Dictionary

n = int(input("Enter size of dictionary: "))
dict = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = int(input("Enter the value: "))
    dict[key] = value       ## to add key-value pair in the empty dictionary(dict = {})

print("Original Dictionary is:", dict)

key = int(input("Enter the key you want to remove: "))

final_dict = {}

for k in dict:
    if(k != key):
        final_dict[k] = dict[k]

print("The Dictionary after removing the key-value pair:", final_dict)