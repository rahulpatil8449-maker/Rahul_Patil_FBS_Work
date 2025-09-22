# Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.

n = int(input("Enter no. of elements: "))
list = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    list += [ele]

print("The Original List is:", list)

even_list = []
odd_list =[]

for i in range(n):
    if(list[i] % 2 == 0):
        even_list += [list[i]]
    else:
        odd_list += [list[i]]

print("The List with the Even elements is:", even_list)
print("The List with the Odd elements is:", odd_list)