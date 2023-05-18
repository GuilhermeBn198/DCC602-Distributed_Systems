import socket
import threading
import base64

SERVIDOR = 'localhost'
PORTA = 5001

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soquete.bind((SERVIDOR, PORTA))

soquete.listen()

clientes = []

apelidos = []

def transmitir(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)

def lidar_cliente(cliente):
    while True:
        try:
            index = clientes.index(cliente)
            apelido = apelidos[index]

            mensagem = cliente.recv(2048)
            mensagem_decodificada = apelido + ': ' + base64.b64decode(mensagem).decode('ascii')
            mensagem_codificada = base64.b64encode(mensagem_decodificada.encode('ascii'))
            transmitir(mensagem_codificada)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[index]
            mensagem = f'{apelido} saiu do chat!'
            print(mensagem)
            mensagem_codificada = base64.b64encode(mensagem.encode('ascii'))
            transmitir(mensagem_codificada)
            apelidos.remove(apelido)
            break

def receber_clientes():
    while True:
        cliente, endereco = soquete.accept()
        print(f'Conectado com {str(endereco)}')

        mensagem_codificada = base64.b64encode('Como voce prefere ser identificado?'.encode('ascii'))

        cliente.send(mensagem_codificada)
        apelido = base64.b64decode(cliente.recv(2048)).decode('ascii')

        apelidos.append(apelido)
        clientes.append(cliente)

        print(f'O cliente tem o apelido {apelido}!')

        mensagem_codificada = base64.b64encode(f'{apelido} entrou no chat!'.encode('ascii'))
        transmitir(mensagem_codificada)

        mensagem_codificada = base64.b64encode('Conectado ao servidor!'.encode('ascii'))
        cliente.send(mensagem_codificada)

        thread = threading.Thread(target=lidar_cliente, args=(cliente,))
        thread.start()

def iniciar_servidor():
    receber_clientes()

iniciar_servidor()
