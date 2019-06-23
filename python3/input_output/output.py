a = 10
b = 20

print(a, b, sep=",")

name = 'Ramon'
marks = 10

print("Name is %s, marks are %.2f" % (name, marks))
print("Name is {}, Marks are {}".format(name, marks))
print(f"Name is {name}, Marks are {marks}")

another_name = 'Albert'
print('My name is {another_name}'.format(another_name=another_name))

another_string = 'Insert text {0} {1}'.format('here', 'LOL')
print(another_string)
