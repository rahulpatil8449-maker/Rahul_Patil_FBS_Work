# Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km=0, mtr=0, cm=0):
        self.km = km
        self.mtr = mtr
        self.cm = cm
        self.normalize()  # Ensure values are consistent
        print(f"Constructor called: Distance created {self}")

    def __del__(self):      # Destructor
        print(f"Destructor called: Distance {self} is being deleted")

    def normalize(self):
        # converting cm to meters
        self.mtr += self.cm // 100
        self.cm = self.cm % 100

        # converting meters to kms
        self.km += self.mtr // 1000
        self.mtr = self.mtr % 1000

    def __add__(self, other):   # Overloading + Operator
        km = self.km + other.km
        mtr = self.mtr + other.mtr
        cm = self.cm + other.cm
        result = Distance(km, mtr, cm)
        result.normalize()
        return result

    def __sub__(self, other):   # Overloading - Operator
        # converting distance into cms
        total1 = (self.km * 100000) + (self.mtr * 100) + self.cm
        total2 = (other.km * 100000) + (other.mtr * 100) + other.cm

        # Subtract and convert back
        diff = abs(total1 - total2)
        km = diff // 100000
        diff = diff % 100000
        mtr = diff // 100
        cm = diff % 100
        return Distance(km, mtr, cm)

    def __str__(self):      # Defining __str__ method
        return f"{self.km} kilometer {self.mtr} meters {self.cm} centimeters\n"

d1 = Distance(2, 750, 80)
d2 = Distance(1, 400, 50)

d3 = d1 + d2  # Overloading + Operator
d4 = d1 - d2  # Overloading - Operator

print("\nOutput will be:")
print(f"{d1} + {d2} = {d3}")
print(f"{d1} - {d2} = {d4}")

del d1
del d2
del d3
del d4
