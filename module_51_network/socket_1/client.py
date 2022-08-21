"""
module: network programming
topic: socket

client-side
"""

import socket

# create a socket object
mysocket = socket.socket()

# connect
mysocket.connect(("127.0.0.1", 8088))

# send data in byte stream
mysocket.send(b'Hi server, I am client.')
res = mysocket.recv(1024)

print(f'Client: received from server {res}')

mysocket.close()