# Write a program to remove all occurrences of a given element in the list.

n = int(input("Enter no. of elements: "))
list = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    list += [ele]

print("The Original List is:", list)

number = int(input("Enter the number to remove all occurences of: "))
new_list = []

for i in range(n):
    if(list[i] != number):
        new_list += [list[i]]
    else:
        print(f"The {number} is not in the List")

print(f"New List after removing all occurence of {number} will be: {new_list}")