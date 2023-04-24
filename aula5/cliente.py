import socket
import threading

def start_client():
    host = "localhost"
    port = 12346

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    connected = True
    while connected:
        msg = input()
        client.sendall(msg.encode())
        if msg == "quit":
            connected = False

    client.close()

start_client()