import time
import socket
import threading

SERVIDOR_ENDERECO = "localhost"
SERVIDOR_PORTA = 5056

class Cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Função para enviar mensagens ao servidor
def enviar_mensagem(client_socket):
    conectado = True
    while conectado:
        mensagem = input("Digite uma mensagem: \n")
        if mensagem == 'sair':
            conectado = False
            print(Cores.WARNING + 'Encerrando aplicação... Agora você pode interromper o processo.' + Cores.ENDC)
        tempo_inicio = time.time()
        client_socket.send(mensagem.encode())
        print("--- Tempo de execução: %s segundos ---" % (time.time() - tempo_inicio))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVIDOR_ENDERECO, SERVIDOR_PORTA))

# Inicia uma thread para enviar mensagens
enviar_thread = threading.Thread(target=enviar_mensagem, args=(client_socket,))
enviar_thread.start()

while True:
    # Recebe mensagens do servidor e as imprime
    mensagem = client_socket.recv(1024).decode()
    print(Cores.OKGREEN + "Mensagem recebida do servidor: " + mensagem + Cores.ENDC)
