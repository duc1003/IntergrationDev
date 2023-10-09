import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(5)

def reverse_and_capitalize(data):
    words = data.split(" ")
    reversed_words = [word[::-1].capitalize() for word in words]
    return ' '.join(reversed_words)

def calculate_sum(data):
    numbers = [int(num) for num in data.split() if num.isdigit()]
    return sum(numbers)

def handle_client(client_socket):
    try:
        while True:
            menu = "\n1. Đảo ngược chuỗi và in hoa ký tự đầu của mỗi từ\n2. Tính tổng các số nguyên\n3. Thoát\nNhập lựa chọn: "
            client_socket.send(menu.encode())
            choice = client_socket.recv(1024).decode()
            if choice == '1':
                data = client_socket.recv(1024).decode()
                result = reverse_and_capitalize(data)
                client_socket.send(result.encode())
            elif choice == '2':
                data = client_socket.recv(1024).decode()
                result = str(calculate_sum(data))
                client_socket.send(result.encode())
            elif choice == '3':
                break
    except Exception as e:
        print(f"error: {e}")
    finally:
        client_socket.close()

print(f"Server is listening on : {host}:{port}")

while True:
    client_socket, client_address = s.accept()

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
