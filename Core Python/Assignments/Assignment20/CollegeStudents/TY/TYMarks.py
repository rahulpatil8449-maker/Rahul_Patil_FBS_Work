# Create another package “TY” which has a class TYMarks (Theory, Practical)

class TYMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def display_tymarks(self):
        print(f'TY Marks => Theory: {self.theory}, Practical: {self.practical}')