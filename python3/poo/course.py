class Course:

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        return sum(self.ratings) / len(self.ratings)


c1 = Course('Learn Java', [1, 3, 5, 6])

print(c1.name)
print(c1.ratings)

print(c1.average())


