# Implement a generator function that yields palindrome numbers. 
# Palindromes are numbers that read the same backward as forward 
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.



def is_palindrome(num):
    return str(num) == str(num)[::-1]   # to reverse the string(num "palindrome")

def palin_generator():  # for infinite palindrome numbers using generator
    num = 0

    while(True):
        if(is_palindrome(num)):
            yield num
        num += 1

print("First 50 Palindrome Numbers are: ")
count = 0

for i in palin_generator():     # to print limited palindrome numbers (here first 50)
    print(i, end = " ")
    count += 1
    if(count == 50):        # stops at 50 not going in infinite loop
        break