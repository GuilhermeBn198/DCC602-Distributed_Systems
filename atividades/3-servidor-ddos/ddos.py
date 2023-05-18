import os
import socket
import threading

SERVIDOR_ENDERECO = "localhost"
SERVIDOR_PORTA = 5056

pid = os.getpid()
print('Número do processo', pid)

_1ByteMensagem = b'\x00'
_512ByteMensagem = b'\x00' * 512
_1024ByteMensagem = b'\x00' * 1024

def receber_mensagem(client_socket):
    while True:
        msg = client_socket.recv(2048).decode('utf-8')
        print(msg+'\n')

def enviar_mensagem(client_socket):
    while True:
        print('enviou')
        mensagem = _1024ByteMensagem
        client_socket.send(mensagem)

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVIDOR_ENDERECO, SERVIDOR_PORTA))

    # Loop para enviar e receber mensagens
    for i in range(1, 10001):
        # Cria uma nova thread para enviar mensagens
        sender_thread = threading.Thread(target=enviar_mensagem, args=(client_socket,))
        # Cria uma nova thread para receber mensagens
        receiver_thread = threading.Thread(target=receber_mensagem, args=(client_socket,))
        # Inicia as threads
        sender_thread.start()
        receiver_thread.start()
