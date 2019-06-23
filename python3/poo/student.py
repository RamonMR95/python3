class Student:
    major = 'CSE'

    def __init__(self, rollnumber, name):
        self.rollnumber = rollnumber
        self.name = name


s1 = Student(1, 'Ramon')
print(s1.rollnumber)
print(s1.name)
print(s1.major)
print(Student.major)

