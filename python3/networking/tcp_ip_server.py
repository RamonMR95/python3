import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("Server Listening on port: ", port)
s.listen(1)  # 1 = number of conns

c, addr = s.accept()
print("Connection from: ", str(addr))

c.send(b"Hello from the server")
c.send("bye".encode())
c.close()

