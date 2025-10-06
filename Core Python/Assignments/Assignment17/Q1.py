class Student:
    def __init__(self, sid, name, age, percentage):     ##parameterized constructor
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage
        # self.calrank()

    def accept(self):
        self.sid = int(input("Enter the Student ID:"))
        self.name = input("Enter the Student Name:")
        self.age = int(input("Enter the Age of the Student:"))
        self.percentage = float(input("Enter the Percentage:"))

    def display(self):
        print("--- Student Details ---")
        print("The Student ID is:", self.sid)
        print("Student Name is:", self.name)
        print("Age of the Student is:", self.age)
        print("Percentage of the Student is:", self.percentage)
        # print("Rank:", self.calrank())

    def calrank(self):
        if(self.percentage >= 90):
            print("1st Rank")
        elif(self.percentage >= 80):
            print("2nd Rank")
        elif(self.percentage >= 75):
            print("3rd Rank")
        elif(self.percentage >= 35):
            print("PASS")
        else:
            print("FAIL")

    def __str__(self):      ## Overriding __str__ method
        # return f"Student({self.sid}, {self.name}, {self.age}, {self.percentage})"
        return f"Student(Name = {self.name}, Percentage = {self.percentage})"

s1 = Student(101, 'Ashish', 22, 80)
s1.display()
s1.calrank()

print(s1)       # overriding __str__ method

s2 = Student(0,'', 0, 0.0)
# s2.accept()
s2.display()
s2.calrank()