def digit_count(num):
    cnt = 0
    while(num > 0):
        num = num // 10
        cnt += 1

    return cnt

def sum_of_pow(num, digits):
    rev = 0
    for i in range(digits):
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem

    return rev

def is_palindrome(num):
    digits = digit_count(num)
    rev = sum_of_pow(num, digits)
    if(rev == num):
        print(f"{num} is palindrome.")
    else:
        print(f"{num} is not palindrome.")

num = int(input("Enter the number to check: "))
is_palindrome(num)