num = int(input("Enter no. of terms: "))

a, b = 0, 1

print(f"Fibonacci series up to {num} terms:")

for i in range(num):
    print(a, end=" ")
    a, b = b, a + b