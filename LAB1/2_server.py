import socket
import os
def start_file_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.56.1', 5000))
    server_socket.listen(1)
    print("File server running...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    files = os.listdir('.')  # List files in current directory
    file_list = "\n".join(files)
    conn.send(file_list.encode())
    conn.close()
start_file_server()
