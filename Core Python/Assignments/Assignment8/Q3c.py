##  1^1 + 2^2 + 3^3+ …… n^n

def pow_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)

    return total

n = int(input("Enter the vlue of n terms: "))
print("The Sum of the Series will be:")
print(pow_series(n))