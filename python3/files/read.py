import os
import sys

if os.path.isfile('file.txt'):
    f = open("file.txt", "r")
    res = f.read()
    f.close()
    print(res)
else:
    print("File does not exist")
    sys.exit()

