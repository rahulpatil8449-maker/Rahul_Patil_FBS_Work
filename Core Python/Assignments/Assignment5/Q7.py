num = int(input("Enter how many prime numbers: "))

count = 0
n = 2

while count < num:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
        count += 1
    n += 1
