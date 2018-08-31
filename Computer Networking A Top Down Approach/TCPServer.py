from socket import *
serverPort = 80
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()

while 1:
    try:
        message = connectionSocket.recv(1024)
    except ConnectionResetError:
        connectionSocket, addr = serverSocket.accept()
        continue
    print('Received Message = ', message.decode('utf-8'))
    if message == str.encode('Kshitij'):
        connectionSocket.send(str.encode("Closing Server!!!"))
        break
    connectionSocket.send(message.upper())
    
connectionSocket.close()
