import socket
import base64

HOST = ''
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

print(f'Servidor escutando na porta {PORT}...')

conn, addr = s.accept()
print(f'Conectado por {addr}')

while True:
    try:
        data = conn.recv(2048)
        message = base64.b64decode(data)
        print(f'Mensagem recebida: {message.decode("ascii")}')

        conn.sendall(base64.b64encode(message))
    except KeyboardInterrupt or BrokenPipeError:
        print("Servidor desligando...")
        conn.close()
        exit()
        