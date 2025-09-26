import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',55555))
server.listen()

while True:
    client,address = server.accept()
    print(f"Connect to {address}")
    client.send("you are connected!".encode())
    client.close()