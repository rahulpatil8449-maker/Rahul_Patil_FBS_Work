##  1!+ 2! + 3! + 4!+….. + n!

def fact_series(n):
    total = 0 
    fact = 1
    for i in range(1, n+1):
        fact *= i
        total += fact

    return total

n = int(input("Enter the n terms: "))
print("The Sum of the Factorial Series will be: ")
print(fact_series(n))