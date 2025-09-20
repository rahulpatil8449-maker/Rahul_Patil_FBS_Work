# Write a program to calculate the m to the power n using recursion

def power(m, n):
    if n == 0:
        return 1
    elif n > 0:
        return m * power(m, n - 1)

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

result = power(base, exponent)
print(f"{base} to the power {exponent} will be: {result}")
