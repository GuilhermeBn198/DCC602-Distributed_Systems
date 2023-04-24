import socket
import threading

def reverse_string(string):
    return string[::-1]

def handle_client(conn, addr, connections):
    print(f"[NEW CONNECTION] {addr} connected.")
    connections.append(conn)

    connected = True
    while connected:
        msg = conn.recv(1024)
        if msg == b"quit":
            connected = False
        else:
            reversed_msg = reverse_string(msg.decode())
            print(f"[{addr}] {msg.decode()} => {reversed_msg}")
            conn.sendall(reversed_msg.encode())

    conn.close()
    connections.remove(conn)
    print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    host = "localhost"
    port = 12346

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}.")

    connections = []
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, connections))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start_server()
