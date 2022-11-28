"""
# Author: Alden Chico
# GitHub username: aldenmchico
# Date: 12/03/22
# Description: Client process for client-chat program
# Sources:
    Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
    https://docs.python.org/3.4/howto/sockets.html
"""

from socket import *

serverPort = 4000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', serverPort))
print(f'Connected to: localhost on port: {serverPort}')
print('Type /q to quit')
print('Enter message to send...')
sendMessage = input('> ')
clientSocket.send(sendMessage.encode())
if sendMessage == '/q':
    clientSocket.close()
else:
    while True:
        recvMessage = clientSocket.recv(1024).decode()
        if recvMessage:
            if recvMessage == '/q':
                print('SERVER TERMINATED THE CHAT')
                clientSocket.close()
                break
            else:
                print(recvMessage)
            sendMessage = input('> ')
            clientSocket.send(sendMessage.encode())
            if sendMessage == '/q':
                clientSocket.close()
                break

