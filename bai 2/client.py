import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.connect((host, port))
str = "Thong tin tu client"
s.send(str.encode('utf-8'))
print("Nhan thong tin moi tu server: ", s.recv(1024))
s.close()