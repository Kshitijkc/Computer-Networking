from socket import *
serverName = '172.20.20.82'
serverPort = 12001
m = True
k = True
while 1:
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        break
    except ConnectionRefusedError:
        if m == True:
            print("Please Wait ...")
            m = False;
    
while 1:
    try:
        message = input('Input lowercase sentence:')
        clientSocket.send(str.encode(message))    
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence.decode('utf-8'))
    except (ConnectionResetError, OSError, ConnectionRefusedError):
        while 1:
            try:
                clientSocket = socket(AF_INET, SOCK_STREAM)
                clientSocket.connect((serverName,serverPort))
                break
            except ConnectionRefusedError:
                if k == True:
                    print("Please Wait ...")
                    k = False
        clientSocket.send(str.encode(message))    
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence.decode('utf-8'))
        k = True
    
    if message == 'Kshitij':
        break
    
print('From Server:', " Closing Client!!!")    
clientSocket.close()
