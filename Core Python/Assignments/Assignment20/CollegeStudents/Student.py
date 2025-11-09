# Create object of student class (Outside SY & TY package) having roll 
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY 
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60, 
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result 
# of the student in proper format.


from SY.SYMarks import SYMarks
from TY.TYMarks import TYMarks

class Student:
    def __init__(self, rollno, name, symarks, tymarks):
        self.rollno = rollno
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

    def calculate(self):
        computer_total = self.symarks.computer_total + self.tymarks.theory

        percentage = computer_total / 2

        if(percentage >= 70):
            grade = 'A'
        elif(percentage >= 60):
            grade = 'B'
        elif(percentage >= 50):
            grade = 'C'
        elif(percentage >= 40):
            grade = 'Pass Class'
        else:
            grade = 'FAIL'

        return computer_total, percentage, grade
    
    def display_all(self):
        print(f'Roll No.: {self.rollno}')
        print(f'Name: {self.name}')
        self.symarks.display_symarks()
        self.tymarks.display_tymarks()

        total, percent, grade = self.calculate()
        print(f'Total (Computer): {total}')
        print(f'Percentage: {percent}')
        print(f'Grade: {grade}')


if(__name__ == '__main__'):
    sy = SYMarks(89, 55, 75)
    ty = TYMarks(93, 76)
    s1 = Student(21, 'Sunil', sy, ty)

    s1.display_all()