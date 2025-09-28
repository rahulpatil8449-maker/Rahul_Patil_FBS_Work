def factor(num):
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i, end = " ")

num = int(input("Enter the number to find factors of: "))
print(f"The factors of {num} are:")
factor(num)