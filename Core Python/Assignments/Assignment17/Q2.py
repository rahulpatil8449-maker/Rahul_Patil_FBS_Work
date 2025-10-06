from Q1 import Student

class EnggStudent(Student):
    def __init__(self, sid, name, age, percentage, branch, intmarks):
        super().__init__(sid, name, age, percentage)
        self.branch = branch
        self.intmarks = intmarks

    def accept(self):
        super().accept()
        self.branch = input("Enter the branch: ")
        self.intmarks = float(input("Enter the internal marks of the Engeneering student: "))

    def display(self):
        print("=== Engineering Student Details ===")
        super().display()
        print("Branch of the student is:", self.branch)
        print("Internal Marks of the student is:", self.intmarks)

    def calrank(self):      ##Overriding
        final_marks = self.percentage + self.intmarks / 2
        if(final_marks >= 90):
            rank = "Distinction"
        elif(final_marks >= 80):
            rank = "1st Class"
        elif(final_marks >= 35):
            rank = "PASS"
        else:
            rank = "FAIL"
        return rank

    def __str__(self):      ##Overriding __str__ method
        return f"EnggStudent(Name : {self.name}, Branch : {self.branch}, Rank of the Student : {self.calrank()})"
    
e1 = EnggStudent(1001, "Anil", 21, 86, "ENTC", 92)
e1.display()

print(e1.calrank())
print(e1)