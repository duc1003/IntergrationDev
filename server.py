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
    path = client_socket.recv(1024).decode('utf-8')
    try:
        print(f"Server is listening on : {host}:{port}")
        data = client_socket.recv(1024).decode('utf-8')   
        allData = data.split('\n')   
        result = "\n"
        for i in range(0, len(allData)-1):
            total = calculate_sum(allData[i])
            result += f"Tổng chuỗi dòng {++i} là: {total} \n"
        client_socket.send(result.encode())
        with open(path, "a") as file:
            file.write(data + "\n")
            
    except IOError as e:
        print(f"Lỗi khi ghi dữ liệu vào tệp: {e}")
    finally:
        client_socket.close()

while True:
    client_socket, addr = s.accept()
    print(f"Kết nối mới từ {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
