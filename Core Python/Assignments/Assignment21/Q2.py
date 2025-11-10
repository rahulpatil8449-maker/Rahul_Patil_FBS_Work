# Create class television that has members to hold the model number ,screen size and price. Take a member function to take input from user, If more than 4 digits 
# are entered for model number, if screen size is smaller than 12 inches or greater than 70 inches or if the price is negative or greater than 5000 Rs, then throw an exception.
# Write a main() that instantiates an object and allows the user to enter and display data. If exception is caught, replace all data member values with zero


class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def accept(self):
        try:
            self.model_no = int(input("Enter the Model Number(max 4 digits): "))
            self.screen_size = float(input("Enter the Screen Size(12 to 70 inches): "))
            self.price = float(input("Enter the price(must be 0 to 5000 Rs.): "))

            if(self.model_no > 9999):
                raise ValueError("Error = Please enter max 4 digits..")
            if(not 12 <= self.screen_size <= 70):
                raise ValueError("Error = Please enter screen size between 12 to 70 inches..")
            if(not 0 <= self.price <= 5000):
                raise ValueError("Error = Please enter price between 0 to 5000..")
            
        except ValueError as ve:
            print("Error:", ve)
            print("Invalid data entered!!")

    def display(self):
        print("\n")
        print(f'Model Number: {self.model_no}')
        print(f'Screen Size: {self.screen_size} inches')
        print(f'Price: Rs.{self.price}')

    
def main():
    t1 = Television()
    t1.accept()
    t1.display()

if(__name__ == '__main__'):
    main()