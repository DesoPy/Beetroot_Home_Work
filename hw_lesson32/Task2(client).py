import socket


"""
Task 2

Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm
by a specific key obtained from the client.
"""


HOST = '127.0.0.1'
PORT = 47047

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    text = input('Enter the text: ')
    key = input('Enter the key(numbers): ')
    MSG = text + '&' + key
    client.sendall(MSG.encode())
    response = client.recv(1024)
    print('Your response - ', response.decode())
