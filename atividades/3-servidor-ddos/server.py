import os
import socket
import threading

pid = os.getpid()
print('Número do processo', pid)
# Endereço e porta do servidor
SERVIDOR_ENDERECO = "localhost"
SERVIDOR_PORTA = 5056

# Lista de clientes conectados
clientes = []
# Função que lida com as mensagens enviadas pelos clientes
def lidar_com_mensagem(client_socket, address):
    while True:
        try:
            mensagem = client_socket.recv(1024).decode()
            if mensagem == 'sair':
                # Remove o cliente da lista quando a conexão é encerrada
                print(f'Cliente {address} desconectou')
                clientes.remove(client_socket)
                break
            print(f"Mensagem recebida de {address}: {mensagem}")
            # Envia a mensagem de volta para todos os clientes conectados
            for c in clientes:
                c.send(mensagem[::-1].encode())
                # if c != client_socket:
                #     c.send(mensagem.encode())
        except:
            # Remove o cliente da lista quando ocorre um erro de conexão
            clientes.remove(client_socket)
            break

# Cria o socket do servidor e configura para aceitar conexões de clientes
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVIDOR_ENDERECO, SERVIDOR_PORTA))
server_socket.listen()

print(f"Servidor iniciado em {SERVIDOR_ENDERECO}:{SERVIDOR_PORTA}")

# Loop principal que aceita conexões de clientes e cria uma thread para cada conexão
while True:
    client_socket, address = server_socket.accept()
    print(f"Novo cliente conectado: {address}")
    # Adiciona o novo cliente à lista de clientes conectados
    clientes.append(client_socket)
    # Cria uma nova thread para lidar com as mensagens do cliente
    thread_mensagem = threading.Thread(target=lidar_com_mensagem, args=(client_socket, address))
    thread_mensagem.start()
