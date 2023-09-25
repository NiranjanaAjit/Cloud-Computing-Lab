import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
print("connected to server",client.getsockname())
#client.send("I am CLIENT\n".encode())
message=""
while message!="bye":
    print("Client:",end=" ")
    message=input()
    client.send(message.encode())
    from_server = client.recv(4096)
    print ("Server:",from_server.decode())
client.close()
