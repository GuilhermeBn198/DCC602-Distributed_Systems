
        
import socket
import base64

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    try:
        message = input('Cliente: ').encode('ascii')
        base64_bytes = base64.b64encode(message)
        
        s.sendall(base64_bytes)

        data = s.recv(2048)

        print(f'Servidor: {base64.b64decode(data).decode("ascii")}')
    except KeyboardInterrupt:
        s.close()
        exit()