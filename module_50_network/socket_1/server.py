"""
module: network programming
topic: socket

server-side
"""
import socket

# create a socket object
mysocket = socket.socket()
# print(mysocket)

# bind
mysocket.bind(("127.0.0.1",8088))

# listen
mysocket.listen()

# waiting for connection from client
conn, address = mysocket.accept()

# receiving data, buffer size = 1024 bytes
data = conn.recv(1024)
print(f'received from client {data}')

conn.send(b'Server listening...')

# closing connection
conn.close()

# closing socket at server
mysocket.close()





