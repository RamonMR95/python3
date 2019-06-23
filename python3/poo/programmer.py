class Programmer:

    def __init__(self, name, salary, technologies):
        self.name = name
        self.salary = salary
        self.technologies = technologies


    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies


p1 = Programmer('Ramon', 2000, 'Java')
print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

p1.setTechnologies('C++')
print(p1.getTechnologies())
