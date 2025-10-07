# Python Program to Concatenate Two Dictionaries Into One

n = int(input("Enter the size of the dictionary1: "))
dict1 = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = input("Enter the value: ")

    dict1[key] = value

print("Dictionary 1 will be:", dict1)

n = int(input("Enter the size of the dictionary1: "))
dict2 = {}

for i in range(n):
    key = int(input("Enter the key: "))
    value = input("Enter the value: ")

    dict2[key] = value

print("Dictionary 2 will be:", dict2)

added_dict = {}     # to store key-value pair of both dict1 & dict2 in added_dict

for key in dict1:
    added_dict[key] = dict1[key]        # to add keys of dict1 in added_dict

for key in dict2:
    added_dict[key] = dict2[key]        # to add keys of dict2 in added_dict

print("Concatinated Dictionary is:", added_dict)