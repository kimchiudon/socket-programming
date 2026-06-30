from socket import *
serverName = 'hostname'
serverPort = 1200

clientSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET은 IPv4를 의미, SOCK_DGRAM은 UDP를 의미함.

message = Input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvform(2048)
print(modifiedMessage.decode())

clientSocket.close()
