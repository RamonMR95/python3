f = open("file.txt", "w")
s = ''


while s != '#':
    s = input("Enter text: ")
    f.write(s + "\n")

f.close()
