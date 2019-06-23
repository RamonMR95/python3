x = 123


def display():
    x = 23
    print(x)
    print(globals()['x'])


display()

z = display
z()

