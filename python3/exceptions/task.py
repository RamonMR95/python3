class InvalidPasswordException(Exception):
    pass


try:
    x = input("Enter you password: ")
    if len(x) < 8:
        raise InvalidPasswordException("Password length must be greater than 8 chars")
except InvalidPasswordException as err:
    print(err)
else:
    print("Your password length is greater than 8 chars")


