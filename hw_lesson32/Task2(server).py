import socket


"""
Task 2

Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm
by a specific key obtained from the client.
"""


HOST = '127.0.0.1'
PORT = 47047


def encrypt(text: str, key: int) -> str:
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key-97) % 26 + 97)
    return result


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()

    with conn:
        data = conn.recv(2048)
        data = data.decode()
        text, key = data.split('&')
        response = encrypt(text, int(key))
        conn.sendall(response.encode())
