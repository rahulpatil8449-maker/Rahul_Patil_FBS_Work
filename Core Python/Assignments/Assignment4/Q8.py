start_num = int(input("Enter the starting number of the range: "))
end_num = int(input("Enter the ending number of the range: "))

print(f"The numbers that are divisible by 7 and 5 in a {start_num} - {end_num} range are:")

for i in range(start_num, end_num + 1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i, end = ' ')