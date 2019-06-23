maths = float(input("Enter you maths marks"))
physics = float(input("Enter you physics marks"))
chemistry = float(input("Enter you chemistry marks"))

if maths < 35 or physics < 35 or chemistry < 35:
    print("You have failed your exams")
elif (maths + physics + chemistry) / 3 <= 59:
    print("Grade C")
elif (maths + physics + chemistry) / 3 <= 69:
    print("Grade B")
else:
    print("Grade A")
