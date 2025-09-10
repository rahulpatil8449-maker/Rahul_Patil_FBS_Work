##  Write a program to check if entered year is a leap year or not.

def check_year(year):
    if(year % 400 == 0 and year % 4 == 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")

    return year

year = int(input("Enter the year to be checked: "))
check_year(year)