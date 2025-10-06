from Q1 import Student

class MedicStud(Student):
    def __init__(self, sid, name, age, percentage, specialization, internshipmarks):
        super().__init__(sid, name, age, percentage)
        self.specialization = specialization
        self.internshipmarks = internshipmarks

    def accept(self):
        super().accept()
        self.specialization = input("Enter the specialization: ")
        self.internshipmarks = float(input("Enter the internship marks: "))

    def display(self):
        print("=== Medical Student Details ===")
        super().display()
        print("Specialization of the student:", self.specialization)
        print("Internship marks of the marks:", self.internshipmarks)

    def calrank(self):      ##Overriding calrank() method
        final_marks = self.percentage + self.internshipmarks / 2
        if(final_marks >= 90):
            rank = "Distinction"
        elif(final_marks >= 80):
            rank = "1st Class"
        elif(final_marks >= 35):
            rank = "PASS"
        else:
            rank = "FAIL"
        return rank
    
    def __str__(self):      ##Overriding __str__method
        return f"Medical Student: (Name : {self.name}, Specialization of the Student : {self.specialization}, Rank of the Student : {self.calrank()})"
    
m1 = MedicStud(103, "Anuj", 19, 82, "Web Development", 76)
m1.display()

print(m1.calrank())
print(m1)