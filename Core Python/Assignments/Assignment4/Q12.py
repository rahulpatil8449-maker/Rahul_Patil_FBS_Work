## Program to print Armstrong numbers in a given range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end} will be: ")

for num in range(start, end + 1):
    count = len(str(num))           # to count the digits
    temp = num

    total = 0
    while(temp > 0):
        rem = temp % 10
        total += rem ** count
        temp = temp // 10
    
    if(total == num):
        print(num)