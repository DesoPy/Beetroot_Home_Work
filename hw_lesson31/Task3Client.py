import socket


"""
Task 3
Echo server with threading

Create a socket echo server that handles each connection using the multiprocessing library.
"""


def connect_to_serv():
    host = '127.0.0.1'
    port = 47047
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    message = input('Enter a message to send to the server: ')
    client.sendall(message.encode('utf-8'))
    response = client.recv(1024)
    print(f"Server responded: {response.decode('utf-8')}")


connect_to_serv()
