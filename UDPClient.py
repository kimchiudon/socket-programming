from socket import * 
serverName = 'hostname'
serverPort = 1200

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = Input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvform(2048)
print(modifiedMessage.decode())

clientSocket.close()
