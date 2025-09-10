##  Sum of all prime numbers between 1 to n

def prime_sum(n):
    total = 0
    for i in range(2, n + 1):
        #total = 0
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            total += i

    return total

n = int(input("Enter the n terms: "))
print(prime_sum(n))