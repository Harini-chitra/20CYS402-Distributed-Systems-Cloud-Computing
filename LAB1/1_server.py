import socket

server_ip = "0.0.0.0"
server_port = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'exit':
        print("Client exited.")
        break
    print("Client:", msg)
    reply = input("Server: ")
    conn.sendall(reply.encode())
    if reply.lower() == 'exit':
        break

conn.close()
