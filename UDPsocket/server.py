import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
# Listen for incoming datagrams
stat=True
while(stat):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    print("Connected to client")
    message = bytesAddressPair[0]
    # print("message aaan ithu :",str(message))
    address = bytesAddressPair[1]
    clientIP  = "Client IP Address:{}".format(address)
    clientMsg = "Client: {}".format(message.decode())
    print(clientMsg)
    print(clientIP)
    while message.decode()!="bye":
        bytesToSend=str.encode(input("Server: "))
        UDPServerSocket.sendto(bytesToSend, address)
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        #address = bytesAddressPair[1]
        #clientIP  = "Client IP Address:{}".format(address)
        clientMsg = "Client: {}".format(message.decode())
        print(clientMsg)
    
    stat=input("wait? y/n: ")
    if stat=="n":
        stat=False
        print("Server shutting down")
    else:
        stat=True
        print("Server waiting for client")