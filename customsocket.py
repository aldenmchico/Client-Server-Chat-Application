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


class MySocket(socket):

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        super().__init__()

    def bind(self, host, port):
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((host, port))

    def connect(self, host, port):
        self.sock.connect((host, port))

    def listen(self, connections):
        self.sock.listen(connections)

    def accept(self):
        return self.sock.accept()

    def send(self, msg):
        self.sock.send(msg.encode())
        """
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        """

    def recv(self):
        return self.sock.recv(1024).decode()
        """
        chunks = []
        bytes_recd = 0
        
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        
        return b''.join(chunks)
        """
    def close(self):
        self.sock.close()
