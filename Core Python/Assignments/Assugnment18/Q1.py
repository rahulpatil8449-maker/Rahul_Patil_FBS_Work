# Create a class Complex Number with data members as real and imag and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self, real=0, imagine=0):      # Constructor
        self.real = real
        self.imagine = imagine
        print(f"Constructor called: Complex number created {self}")

    def __del__(self):      # Destructor
        print(f"Destructor called: Complex number {self} is being deleted")

    def __add__(self, other):       # Overloading + Operator
        return ComplexNumber(self.real + other.real, self.imagine + other.imagine)

    def __sub__(self, other):       # Overloading - Operator
        return ComplexNumber(self.real - other.real, self.imagine - other.imagine)

    def __str__(self):
        if(self.imagine >= 0):
            return f"{self.real} + {self.imagine}i"
        else:
            return f"{self.real} - {abs(self.imagine)}i"


c1 = ComplexNumber(2, 4)
c2 = ComplexNumber(1, -3)

c3 = c1 + c2   # Overloading + operator here
c4 = c1 - c2   # Overloading - operator here

print("\nResult will be:")
print(f"{c1} + {c2} = {c3}")
print(f"{c1} - {c2} = {c4}")

del c1
del c2
del c3
del c4
