
try:
    x = int(input("Enter an even number: "))
    assert x % 2 == 0, "You have entered an odd number"
except AssertionError as err:
    print(err)
