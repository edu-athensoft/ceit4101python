"""
module: network programming
topic: socket

server-side
"""
import socket

import time

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
while True:
    try:
        data = conn.recv(1024)
        print(f'received from client {data}')
        # conn.send(b'Server listening...')
        time.sleep(1)
        msg = str(data, 'utf-8')
        if msg.strip() == 'bye':
            # closing connection
            conn.close()
            break
    except Exception as e:
        print(e)
        # break
        # pass




# closing socket at server
mysocket.close()





