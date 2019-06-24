x = int(input("Enter a number greater than 10: "))

if x <= 10:
    raise Exception(f"Number {x} is less than 10")
else:
    print(x)



