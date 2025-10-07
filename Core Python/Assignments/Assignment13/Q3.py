# Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}
print("Original Dictionary is:", dict)

key = int(input("Enter the key you want to search: "))

if key in dict:
    print("Key exists in dictionary...")
else:
    print("Key doesn't exist in dictionary!!!")