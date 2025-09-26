import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind(('127.0.0.1',55554))
client.connect(('127.0.0.1',55555))
message = client.recv(1024)

print(message)