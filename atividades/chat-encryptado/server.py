import socket
import threading
import base64

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()

clients = []  # Lista para armazenar os clientes conectados

nicknames = []  # Lista para armazenar os apelidos dos clientes


def broadcast(message):
    # Envia a mensagem para todos os clientes conectados
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            index = clients.index(client)
            nickname = nicknames[index]

            # Recebe a mensagem do cliente
            message = client.recv(2048)

            # Decodifica a mensagem
            decoded_message = nickname + ': ' + \
                base64.b64decode(message).decode('ascii')

            # Codifica a mensagem novamente
            encoded_message = base64.b64encode(decoded_message.encode('ascii'))

            # Envia a mensagem codificada para todos os clientes
            broadcast(encoded_message)
        except:
            # Caso ocorra uma exceção, provavelmente o cliente desconectou

            index = clients.index(client)

            # Remove o cliente da lista de clientes
            clients.remove(client)

            # Fecha a conexão com o cliente
            client.close()

            nickname = nicknames[index]

            # Mensagem informando que o cliente saiu do chat
            message = f'{nickname} saiu do chat!'
            print(message)

            # Codifica a mensagem
            encoded_message = base64.b64encode(message.encode('ascii'))

            # Envia a mensagem codificada para todos os clientes
            broadcast(encoded_message)

            # Remove o apelido do cliente da lista de apelidos
            nicknames.remove(nickname)
            break


def receive():
    while True:
        # Aceita a conexão do cliente
        client, address = s.accept()
        print(f'Conectado com {str(address)}')

        # Envia uma mensagem solicitando o apelido do cliente
        encoded_message = base64.b64encode(
            'Como você prefere ser identificado?'.encode('ascii'))

        client.send(encoded_message)

        # Recebe o apelido do cliente
        nickname = base64.b64decode(client.recv(2048)).decode('ascii')

        # Adiciona o apelido do cliente à lista de apelidos
        nicknames.append(nickname)

        # Adiciona o cliente à lista de clientes
        clients.append(client)

        print(f'Nome do cliente é {nickname}!')

        # Mensagem informando que o cliente entrou no chat
        encoded_message = base64.b64encode(
            f'{nickname} entrou no chat!'.encode('ascii'))
        broadcast(encoded_message)

        # Envia uma mensagem de confirmação ao cliente
        encoded_message = base64.b64encode(
            'Conectado ao servidor!'.encode('ascii'))
        client.send(encoded_message)

        # Inicia uma nova thread para lidar com as mensagens do cliente
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
