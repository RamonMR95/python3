import socket

host = "localhost"
port = 4000

s = socket.socket()
s.connect((host, port))

fileName = input("Enter a file name: ")

s.send(fileName.encode())

content = s.recv(1024)
print(content.decode())

s.close()
