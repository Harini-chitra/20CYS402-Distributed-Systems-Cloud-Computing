import socket
def connect_to_peer():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.56.1', 5000))
    data = client_socket.recv(4096).decode()
    print("Available files on server:\n", data)
    client_socket.close()
connect_to_peer()
