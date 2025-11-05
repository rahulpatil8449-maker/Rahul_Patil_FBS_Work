# Develop a memoization decorator that caches the results of function 
# calls and returns the cached result when the same inputs occur again. 
# This can greatly improve the performance of recursive or 
# computationally intensive functions.

## From ChatGPT
# Memoization Decorator

def memoize(func):
    """A decorator that caches results of function calls."""
    cache = {}  # Dictionary to store results

    def wrapper(*args):
        # If result is already in cache, return it
        if args in cache:
            print(f"Fetching from cache for args {args}")
            return cache[args]

        # Otherwise, compute and store it
        result = func(*args)
        cache[args] = result
        print(f"Caching result for args {args}")
        return result

    return wrapper


# Example: Recursive Fibonacci using memoization
@memoize
def fibonacci(n):
    """Return nth Fibonacci number (recursive)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# --- Main Program ---
num = int(input("Enter a number: "))
print(f"Fibonacci({num}) =", fibonacci(num))
