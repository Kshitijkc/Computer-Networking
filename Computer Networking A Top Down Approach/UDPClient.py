from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    message = input('Input lowercase sentence:')
    message = str.encode(message)
    clientSocket.sendto(message,(serverName, serverPort))
    if message == str.encode('Kshitij'):
        break
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print( modifiedMessage.decode('utf-8'))
    
clientSocket.close()
print('TATA')
