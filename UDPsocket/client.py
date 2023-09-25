import socket


serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
message=""

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while message!="bye":
    message=input("Client: ")
    bytesToSend= str.encode(message)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    if message=="bye":
        break
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Server: {}".format(msgFromServer[0].decode())
    print(msg)
print("Client shutting down")