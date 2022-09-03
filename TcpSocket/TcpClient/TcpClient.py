from asyncio import Server
import socket
ServerName='localhost'
ServerPort=8964
ClientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ClientSocket.connect((ServerName,ServerPort))
while True:
    sentence=input('input your sentence:\n')
    ClientSocket.send(sentence.encode())
    modifiedmessage=ClientSocket.recv(1024)
    print('upper is:',modifiedmessage.decode())
ClientSocket.close()