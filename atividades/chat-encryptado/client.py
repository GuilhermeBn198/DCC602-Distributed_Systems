import sys
import socket
import threading
import base64

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))


def receive():
    while True:
        try:
            # Recebe os dados do servidor
            data = s.recv(2048)

            if not data:
                # Se os dados estiverem vazios, indica que a conexão foi encerrada
                break
            else:
                # Decodifica e exibe os dados recebidos
                decoded_data = base64.b64decode(data).decode('ascii')
                sys.stdout.write('\033[K' + decoded_data + '\r\n')
        except:
            # Se ocorrer uma exceção, fecha a conexão e encerra o programa
            s.close()
            exit()


def send():
    while True:
        try:
            # Lê a entrada do usuário e envia para o servidor
            message = input().encode('ascii')
            base64_bytes = base64.b64encode(message)
            s.sendall(base64_bytes)
        except:
            # Se ocorrer uma exceção, fecha a conexão e encerra o programa
            s.close()
            exit()


# Inicia uma thread para receber dados do servidor
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Inicia uma thread para enviar dados para o servidor
send_thread = threading.Thread(target=send)
send_thread.start()
