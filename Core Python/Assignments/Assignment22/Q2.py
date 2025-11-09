# WAP a menu driven program to perform following operations using files :
# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records



import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"Employee ID: {self.eid}, Employee Name: {self.ename}, Basic Salary: Rs.{self.basic}")

## adding record
def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    emp = Emp(eid, ename, basic)

    try:
        with open("employees.txt", "rb") as fp:
            data = pickle.load(fp)
    except (FileNotFoundError, EOFError):
        data = []

    data.append(emp)

    with open("employees.txt", "wb") as fp:
        pickle.dump(data, fp)

    print("\n Record added successfully....\n")

## displaying record
def display_all():
    try:
        with open("employees.txt", "rb") as fp:
            data = pickle.load(fp)
    except(FileNotFoundError, EOFError):
        print("\n No records found...\n")
        return

    print("\n\t\t All Employee Records")
    for emp in data:
        emp.display()

## searching record
def search_record():
    try:
        with open("employees.txt", "rb") as f:
            data = pickle.load(f)
    except (FileNotFoundError, EOFError):
        print("\n No records found.\n")
        return

    eid = int(input("Enter Employee ID to search: "))
    found = False

    for emp in data:
        if emp.eid == eid:
            print("\n Record found:\n")
            emp.display()
            found = True
            break

    if not found:
        print("\n Record not found.\n")

## deleting record
def delete_record():
    try:
        with open("employees.txt", "rb") as f:
            data = pickle.load(f)
    except (FileNotFoundError, EOFError):
        print("\n No records found.\n")
        return

    eid = int(input("Enter Employee ID to delete: "))
    new_data = [emp for emp in data if emp.eid != eid]

    if len(new_data) == len(data):
        print("\n Record not found.\n")
    else:
        with open("employees.txt", "wb") as f:
            pickle.dump(new_data, f)
        print("\n Record deleted successfully.\n")

## editing records by Employee ID
def edit_record():
    try:
        with open("employees.txt", "rb") as f:
            data = pickle.load(f)
    except (FileNotFoundError, EOFError):
        print("\nNo records found.\n")
        return

    eid = int(input("Enter Employee ID to edit: "))
    found = False

    for emp in data:
        if emp.eid == eid:
            print("\nCurrent details:")
            emp.display()
            emp.ename = input("Enter new name: ")
            emp.basic = float(input("Enter new basic salary: "))
            found = True
            break

    if found:
        with open("employees.txt", "wb") as f:
            pickle.dump(data, f)
        print("\nRecord updated successfully.\n")
    else:
        print("\nRecord not found.\n")


def main():
    while True:
        print("\t\t Employee Management System ")
        print("1. Add Record")
        print("2. Search Record by ID")
        print("3. Delete Record by ID")
        print("4. Edit Record by ID")
        print("5. Display all Records")
        print("6. Exit")

        choice = input("Enter your choice from (1-6): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            search_record()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            edit_record()
        elif choice == '5':
            display_all()
        elif choice == '6':
            print("\n Exited program. Thank You for choosing US!!!")
            break
        else:
            print("\n Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()