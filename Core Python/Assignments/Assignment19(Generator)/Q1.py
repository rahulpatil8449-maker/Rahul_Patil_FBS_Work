# We want to generate Fibonacci numbers up to a certain limit. 
# Instead of computing and storing the entire sequence in memory, 
# create generator to yield Fibonacci numbers one by one, 
# conserving memory and allowing for easy iteration.



def fib(num):
    a, b = 0, 1
    while(a <= num):
        yield a     # using generator
        a, b = b, a + b

num = int(input("Enter the limit for the Fibonacci Numbers: "))

for result in fib(num):
    print(result, end = " ")