"""
module: network programming
topic: socket

client-side
"""

import socket

import random

# create a socket object
mysocket = socket.socket()

# connect
mysocket.connect(("127.0.0.1", 8088))

# send data in byte stream
# data = 'Hi server, I am client. '+str(random.randint(0, 100))
data = b'Hi server, I am client. '
# data = bytes(data, encoding="utf-8")
mysocket.send(data)
# res = mysocket.recv(1024)
# print(f'Client: received from server {res}')
print('sent')

data = b'bye'
mysocket.send(data)
print('sent')
# res = mysocket.recv(1024)
# print(f'Client: received from server {res}')

mysocket.close()
