
from socket import * 
ServerPort = 8964
ServerSocket = socket(AF_INET,SOCK_DGRAM)
ServerSocket.bind(('',ServerPort))
print('Server ready to run')
while True:
    Message,ClientAddress=ServerSocket.recvfrom(2048)
    print (Message)
    modifiedmessage=Message.decode().upper()
    ServerSocket.sendto(modifiedmessage.encode(),ClientAddress)