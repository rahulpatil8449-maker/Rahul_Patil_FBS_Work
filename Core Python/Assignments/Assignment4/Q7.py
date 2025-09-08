num = int(input("Enter the number: "))

print(f"The integers upto {num} that are not divisible by 3 and 2 are:")

for i in range(1, num + 1):
    if(i % 3 != 0 and i % 2 != 0):
        print(i, end = ' ')