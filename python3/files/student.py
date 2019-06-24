class Student:

    def __init__(self, dni, name, marks):
        self.dni = dni
        self.name = name
        self.marks = marks

    def display(self):
        print(self.dni, self.name, self.marks)


