from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, no_of_person):
        self.no_of_person = no_of_person

    @abstractmethod
    def calculate_toll(self):
        pass



class TwoWheeler(Vehicle):
    def calculate_toll(self):
        toll = 20
        if(self.no_of_person > 2):
            toll += (self.no_of_person - 2) * 10
        return toll



class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        toll = 30
        if(self.no_of_person > 3):
            toll += (self.no_of_person - 3) * 20
        return toll



class FourWheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if(self.no_of_person > 4):
            toll += (self.no_of_person - 4) * 40
        return toll



class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if(self.no_of_person > 6):
            toll += (self.no_of_person - 6) * 100
        return toll


def main():
    while(True):
        print("\nCalculating Toll for Vehicle :- ")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exited. ThankYou !!!!")
            break

        
        person = int(input("Enter no of persons: "))

        if choice == '1':
            vehicle = TwoWheeler(person)
        elif choice == '2':
            vehicle = ThreeWheeler(person)
        elif choice == '3':
            vehicle = FourWheeler(person)
        elif choice == '4':
            vehicle = HeavyVehicle(person)
        else:
            print("Invalid choice! Try again.")
            continue

        toll = vehicle.calculate_toll()
        print(f"Total Toll: Rs. {toll}")



if __name__ == "__main__":
    main()