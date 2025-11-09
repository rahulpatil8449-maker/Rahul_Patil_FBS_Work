# Create a class Emp (eid,ename,basic)


import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f'Employee ID: {self.eid}')
        print(f'Employee Name: {self.ename}')
        print(f'Employee Basic Salary: {self.basic}')

    def __del__(self):
        print(f'Destructor Object for "{self.ename}" called successfully..')

e1 = Emp(101, 'Raj', 35000)
e2 = Emp(102, "Sunil", 50000)

with open('Assignments/Assignment22/employee.txt', 'wb') as fp:
    pickle.dump([e1, e2], fp)
print("Emplyee data Pickled Successfully...\n")


with open('Assignments/Assignment22/employee.txt', 'rb') as fp:
    employee = pickle.load(fp)
print("Employee data Unpickled Successfully...\n")

for emp in employee:
    emp.display()
    print()