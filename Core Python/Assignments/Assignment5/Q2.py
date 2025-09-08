num = int(input("Enter no. of students: "))

avg_total = 0

for i in range(1, num + 1):
    print("Enter marks of 5 subjects: ")
    s1 = float(input("Enter marks of Subject 1: "))
    s2 = float(input("Enter marks of Subject 2: "))
    s3 = float(input("Enter marks of Subject 3: "))
    s4 = float(input("Enter marks of Subject 4: "))
    s5 = float(input("Enter marks of Subject 5: "))

    total = s1 + s2 + s3 + s4 + s5

    percentage = total/500 * 100
    print(f"The Percentage of student {i} will be: {percentage}%.")

avg_total = percentage / num
print("The Average Percentage of Students will be:", avg_total, "%")