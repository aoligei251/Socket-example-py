
from socket import *
import time
ServerName='localhost'
ServerPort = 8964
ClientSocket = socket(AF_INET,SOCK_DGRAM)
i=0
while True:
    #message=input('type you message:\n')
    time.sleep(1)
    message='message number :'+str(i)
    i=i+1
    ClientSocket.sendto(message.encode(),(ServerName,ServerPort))
    ModifiedMessage,ServerAddress=ClientSocket.recvfrom(2018)
    print(ModifiedMessage.decode())

ClientSocket.close()

