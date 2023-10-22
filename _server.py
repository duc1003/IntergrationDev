import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
server_socket.bind((host, port))
server_socket.listen(5)

def reverse_and_capitalize(data):
    words = data.split(" ")
    reversed_words = [word[::-1].capitalize() for word in words]
    return ' '.join(reversed_words)

def calculate_sum(data):
    numbers = [int(num) for num in data.split() if num.isdigit()]
    return sum(numbers)

def handle_client(client_socket): 
    try :
        print(f"Server is listening on: {host}:{port}")
    except IOError as e:
        print(f"Error: {e}")
    finally: 
        client_socket.close()        


while True:
    client_socket, address = server_socket.accept()
    print(f"Allow new access from {address} with port {port}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket, ))
    client_handler.start()