# Write a generator function that mimics the behavior of the built-in 
# range() function. The generator should take start, stop, and step 
# arguments and yield numbers within the specified range.


def my_range(start, stop=None, step=1):
    if stop is None:    # Handling the case where only one argument is passed
        stop = start
        start = 0

    # Raising ValueError if step is zero(0)
    # if step == 0:
    #     raise ValueError("step must not be zero")

    if step > 0:        # for positive steps
        while start < stop:
            yield start
            start += step
    elif(step == 0):
        raise ValueError("Step must not be a Zero(0)!!")
    else:       # for negative steps
        while start > stop:
            yield start
            start += step

print("The result will be for mimicing the range() function:")

for num in my_range(1, 50, 2):
    print(num, end=" ")