## N + N^2 + N^3+N^4 …..+N^N 

N = int(input("Enter the value of N: "))

total = 0

for i in range(1, N + 1):
    total += N ** i

print("The Sum of the following series will be:", total)