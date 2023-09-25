import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
print("server on at ",serv.getsockname())
serv.listen(5)
stat=True
while stat:
  print("waiting for client")
  conn, addr = serv.accept()
  from_client = ''
  data=""
  while data!="bye":
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    print ("Client:",from_client)
    print("Server:",end=" ")
    message=input()
    conn.send(message.encode())
    from_client = ''
    #conn.send("I am SERVER\n".encode())
  conn.close()
  stat=input("wait? y/n: ")
  if stat=="n":
    stat=False
  else:
    stat=True
print ('client disconnected and shutdown')