class Student:
    def __init__(self, dni, name):
        self.__dni = dni
        self.__name = name

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


s1 = Student('5555', 'Ramon')
print(s1.get_dni())
print(s1.get_name())
print(s1._Student__dni)

