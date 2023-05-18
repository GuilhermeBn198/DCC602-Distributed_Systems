import sys
import socket
import threading
import base64

SERVIDOR = 'localhost'
PORTA = 5001

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soquete.connect((SERVIDOR, PORTA))

def receber():
    while True:
        try:
            dados = soquete.recv(2048)
            
            if not dados:
                break
            else:
                dados_decodificados = base64.b64decode(dados).decode('ascii')
                sys.stdout.write('\033[K' + dados_decodificados + '\r\n')
        except:
            soquete.close()
            exit()

def enviar():
    while True:
        try:
            mensagem = input().encode('ascii')
            bytes_base64 = base64.b64encode(mensagem)
            soquete.sendall(bytes_base64)
        except:
            soquete.close()
            exit()

thread_receber = threading.Thread(target=receber)
thread_receber.start()

thread_enviar = threading.Thread(target=enviar)
thread_enviar.start()
