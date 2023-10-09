import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(5)

while True:
    c, address = s.accept()
    print("Da chap nhan ket noi tu ", address)
    output = c.recv(1024)
    print(output)
    c.send(output)
    c.close()
