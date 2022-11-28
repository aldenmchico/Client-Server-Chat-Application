"""
# Author: Alden Chico
# GitHub username: aldenmchico
# Date: 12/03/22
# Description: Server process for client-chat program
# Sources:
    Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
    https://docs.python.org/3.4/howto/sockets.html
"""

from socket import *

serverPort = 4000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('localhost', serverPort))  # Bind the process to localhost port 4000
serverSocket.listen(1)
print(f'Server listening on: localhost on port: {serverPort}')  # Write a message on the console server is running
connectionSocket, addr = serverSocket.accept()
print(f'Connected by ({addr}')
recvMessage = connectionSocket.recv(1024).decode()
print('Type /q to quit')
print('Waiting for message...')
while True:
    if recvMessage:
        if recvMessage == '/q':
            print('CLIENT TERMINATED THE CHAT')
            break
        else:
            print(recvMessage)
        sendMessage = input('> ')
        connectionSocket.send(sendMessage.encode())
        if sendMessage == '/q':
            connectionSocket.close()
            break
    recvMessage = connectionSocket.recv(1024).decode()
