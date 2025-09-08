## 1! + 2! + 3! + .....+ n!

n = int(input("Enter the value of n: "))

fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i          
    total += fact      

print("Sum of series:", total)
