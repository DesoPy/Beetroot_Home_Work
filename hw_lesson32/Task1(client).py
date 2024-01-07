import socket

"""
Task 1

During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.
"""

HOST = '127.0.0.1'
PORT = 47047

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(b'Test', (HOST, PORT))
    data, addr = client.recvfrom(1024)
    print(f'Client got response {data} from server {addr}')
