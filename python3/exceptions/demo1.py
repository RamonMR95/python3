import logging

logging.basicConfig(filename="err_log.log", level=logging.DEBUG)

try:
    f = open("file", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a / b
    logging.info("Division in progress")
    f.write("Writing %d" % c)
except ZeroDivisionError:
    print("Division by zero not allowed")
    logging.error("Division by zero")
else:
    print("You have entered a non zero number")
finally:
    f.close()

