import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.connect((host, port))
while True:
    menu = s.recv(1024).decode('utf-8')
    print(menu)
    choice = input()
    s.send(choice.encode())
    if choice == '1':
        data = input("enter your string: ")
        s.send(data.encode())
        result = s.recv(1024).decode()
        print(f"Kết quả: {result}\n")
    elif choice == '2':
        data = input("enter your string of integers (separated by spaces): ")
        s.send(data.encode())
        result = s.recv(1024).decode()
        print(f"total of string of integer: {result}\n")
    elif choice == '3':
        print("Disconnected.")
        break
s.close()

