## Sum of all odd numbers between 1 to n

def odd_sum(num):
    total = 0
    for i in range(1, num + 1):
        if(i % 2 != 0):
            total += i
        
    return total

num = int(input("Enter the n terms: "))
print(f"The Sum of all the odd numbers till {num} are:")
print(odd_sum(num))