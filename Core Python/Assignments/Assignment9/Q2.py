# # Write a program to check if given number is Armstrong or not using recursive function.

# def digit_count(num):
#     cnt = 0
#     if(num < 0):
#         return 0
    
#     num = num // 10
#     cnt = cnt + 1
    
#     return cnt

# def sum_of_power(num, cnt):
#     sum = 0
#     if(num < 0):
#         return 0
    
#     rem = num % 10
#     sum = sum + (rem ** cnt)
#     num = num // 10

#     return sum

# def is_armstrong(num):
#     cnt = digit_count(num)
#     sum = sum_of_power(num, cnt)
#     if(sum == num):
#         print(f"{num} is an Armstrong Number.")
#     else:
#         print(f"{num} is not an Armstrong Number.")

# num = int(input("Enter the number: "))

# is_armstrong(num)



def armstrong(num, pow):
    if num == 0:
        return 0
    return (num % 10) ** pow + armstrong(num // 10, pow)

n = int(input("Enter a number: "))
digits = len(str(n))

if armstrong(n, digits) == n:
    print(f"{n} is an Armstrong Number.")
else:
    print(f"{n} is not an Armstrong Number.")
