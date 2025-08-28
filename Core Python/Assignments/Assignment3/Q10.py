gender = input("Enter the gender in (M/F): ")
age = int(input("Enter the age: "))

if(gender == 'M'):
    if(age >= 21):
        print("Eligible for marraige.")
    else:
        print("Not Eligible for marraige.")
else:
    if(age >= 18):
        print("Eligible for marraige.")
    else:
        print("Not Eligible for marraige.")
