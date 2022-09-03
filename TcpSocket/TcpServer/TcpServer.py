import _thread
import socket
ServerPort=8964
ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerSocket.bind(('',ServerPort))
ServerSocket.listen(64)

print('server is ready')
#_thread.start_new_thread ( function, args[, kwargs] )
connectionScoket,addr=ServerSocket.accept()
while True:
    try:
        sentence = connectionScoket.recv(1024).decode()
    except:
        connectionScoket.close()

    capitalizedsentence=sentence.upper()
    connectionScoket.send(capitalizedsentence.encode())

connectionScoket.close()