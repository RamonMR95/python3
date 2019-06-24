# DUMPING AN OBJECT TO A FILE
import pickle
import files.student as s

f = open("student.dat", "wb")        # CREATING THE FILE
s1 = s.Student(123, 'Ramon', 10)     # CREATING THE STUDENT
pickle.dump(s1, f)                   # DUMPING THE OBJECT TO THE FILE
f.close()                            # CLOSING THE STREAM


