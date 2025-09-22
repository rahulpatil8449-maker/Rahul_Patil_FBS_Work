# Accept a number from user and check if this element is present in the list or not.Also tell how many times it is present in the list.

n = int(input("Enter no. of elements: "))
l = []

for i in range(n):
    ele = int(input("Enter the elements: "))
    l += [ele]

print("The Original List is:", l)

number = int(input("Enter the number to check in the list: "))
count = 0
found = False

for i in range(n):
    if(l[i] == number):
        found = True
        count += 1
if(found == True):
    print(f"{number} is present in the list and it occurs {count} times.")
else: 
    print(f"{number} is not in the list.")