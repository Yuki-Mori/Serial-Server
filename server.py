from datetime import datetime
import socket
import sys

from server_thread import ServerThread


args = sys.argv
port_num = 0
if len(args) >= 2:
    port_num = args[1]

address = ('localhost', int(port_num))
max_size = 1000


print('[Server]: Starting the server at', datetime.now())
print('[Server]: Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print('[Server]:', server.getsockname())
server.listen(5)

while True:

    client, addr = server.accept()

    thread = ServerThread(client, addr)

    thread.start()
    print('Do you close the server? [Y|n]: ')
    ans = input()
    if ans == 'y' or ans == 'Y':
        break

server.close()
