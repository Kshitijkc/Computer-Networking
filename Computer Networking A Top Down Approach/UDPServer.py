from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Received message = ', message)
    if message == str.encode('Kshitij'):
        break
    modifiedMessage = message.upper()
    print('Replyed message = ', modifiedMessage)
    serverSocket.sendto(modifiedMessage, clientAddress)

print('Bye Bye !!!')
