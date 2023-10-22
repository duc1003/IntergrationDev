import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

client_socket.connect((host, port))
def server_handle() :
    try :
        print("client")
    except IOError as e :
        print(f"Error: {e}")
    finally:
        client_socket.close()
        
server_handle()        
                
