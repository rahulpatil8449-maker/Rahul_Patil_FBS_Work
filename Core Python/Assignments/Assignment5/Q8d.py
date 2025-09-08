## S = a + a^2 / 2 + a^3 / 3 + …… + a^10 / 10

n = int(input("Enter the value of n: "))

S = 0

for i in range(1, 11):
    S = S + (n ** i) / i

print(f"The sum of the following series till {n} will be: {S}.")