import socket

server_ip = input("Enter Server IP Address: ")
server_port = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    msg = input("Client: ")
    client_socket.sendall(msg.encode())
    if msg.lower() == 'exit':
        break
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)
    if reply.lower() == 'exit':
        break

client_socket.close()
