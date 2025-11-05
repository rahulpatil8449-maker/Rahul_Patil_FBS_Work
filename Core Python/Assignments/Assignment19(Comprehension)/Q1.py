# Find all of the numbers from 1–1000 that are divisible by 8


num = [i for i in range(1, 1001) if i % 8 == 0]
print(f'There are "{len(num)}" numbers present between 1 to 1000 that are divisible by 8')
print(num)