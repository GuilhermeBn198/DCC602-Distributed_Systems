# Unica conxeo
import socket
from threading import Thread

def send_message(client, msg):
  client.sendall(msg.encode())

def start_client():
    host = "localhost"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    connected = True
    while connected:
        msg = input('Message: ')
        if msg == "quit":
            connected = False
        n = input('Times(DDOS): ')
        messagesList = list()
        for i in range(int(n)):
          subMessage = Thread(target=send_message, args=(client, f'{msg}, time: {i}',))
          messagesList.append(subMessage)
        for s in messagesList: s.start()
        for s in messagesList: s.join()

    client.close()

start_client()