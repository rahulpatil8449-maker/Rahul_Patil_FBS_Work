start_num = int(input("Enter the starting number of the range: "))
end_num = int(input("Enter the ending number of the range: "))
j = int(input("Enter the number that will be used as a divisor for the numbers in the range: "))

print(f"The numbers that are divisible by {j} in a {start_num} - {end_num} range are:")

for i in range(start_num, end_num + 1):
    if(i % j == 0):
        print(i, end = ' ')