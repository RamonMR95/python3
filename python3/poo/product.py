class Product:

    def __init__(self):
        self.name = 'Zowie'
        self.description = 'BEST MOUSE EVER'
        self.price = 60

    def display(self):
        print(self.name, self.description, self.price)


p1 = Product()

print(p1.name)
print(p1.description)
print(p1.price)

p1.display()

