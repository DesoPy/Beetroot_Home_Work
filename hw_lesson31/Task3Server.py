import socket
import threading


"""
Task 3
Echo server with threading

Create a socket echo server that handles each connection using the multiprocessing library.
"""


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()


def start_serv():
    host = '127.0.0.1'
    port = 47047
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f'[LISTENING] Server is listening on {host}:{port}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


start_serv()
