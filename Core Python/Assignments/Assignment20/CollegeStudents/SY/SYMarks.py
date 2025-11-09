# create a package “SY” which has class SYMARKS (Computer Total, MathsTotal, ElectronicsTotal).

class SYMarks:
    def __init__(self, computer_total, math_total,electronics_total):
        self.computer_total = computer_total
        self.math_total = math_total
        self.electronics_total = electronics_total

    def display_symarks(self):
        print(f'SY Marks => Computer Total: {self.computer_total}, Maths Total: {self.math_total}, Electronics Total: {self.electronics_total}')