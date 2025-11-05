# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.


count_num = [num for num in range(1, 1001) for div in range(2, 10) if num % div == 0]
count_num = set(count_num)      ## to not getting the repeated divisible numbers like(12 = 2,3,4,6)
print("The numbers divisible be single digit numbers are:", count_num)