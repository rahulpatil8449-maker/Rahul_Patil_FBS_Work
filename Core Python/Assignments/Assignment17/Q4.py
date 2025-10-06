class Student:      ## Base Class
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def display(self):
        print(f"Student ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}")

    def __str__(self):
        return f"Student(ID : {self.StudentId}, Name : {self.Name}, Percentage : {self.Percentage})"




class College:      ## College Class
    def __init__(self, total_students):     # Parameterized constructor
        self.total_students = total_students
        self.students = []      # storing students in a list

    def addStudent(self, student):      # Adding student
        if len(self.students) < self.total_students:
            self.students.append(student)
            print(f"Student '{student.Name}' added successfully.")
        else:
            print("Cannot add more students college seats are full !!!")

    def getStudent(self, student_id):       # getting student details by there ID
        for s in self.students:
            if s.StudentId == student_id:
                return s
        return None

    def removeStudent(self, student_id):        # removing student details by their ID
        for s in self.students:
            if s.StudentId == student_id:
                self.students.remove(s)
                print(f"Student {s.Name} removed successfully.")
                return
        print("Student not found !!!")

    def __str__(self):      # Override __str__ method to display/show student details
        if not self.students:
            return "No student in college."
        result = "\n=== List of College Students ===\n"

        for s in self.students:
            result += str(s) + "\n"
        return result


print("=== College Management Program ===")

college = College(3)

s1 = Student(101, "Riya", 20, 85)
s2 = Student(102, "Rahul", 22, 78)
s3 = Student(103, "Sneha", 21, 92)

# Adding students
college.addStudent(s1)
college.addStudent(s2)
college.addStudent(s3)

# Displaying all students details
print(college)

# Getting one student/student details
stud = college.getStudent(102)
if stud:
    print(f"\nStudent Found : {stud.Name}, Percentage : {stud.Percentage}")
else:
    print("\nStudent not found !!!")

# Removig a student/student details
college.removeStudent(101)

# Displaying updated list
print("\nAfter removal :-")
print(college)