import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "89.178.98.66"  # get ip address of this computer
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # [family sock,type sock]
server.bind(ADDR)  # bind this sock to this addr so anyone whos connect this addr will have this sock


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(
            FORMAT)  # tells us how long is msg that comming. decode means "decode this msg from bytes format to string usingthis format"
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)  # how many bytes we gonna receive from the actual msg
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}  {threading.currentThread()}")
            conn.send("Hello there".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER} ")
    while True:  # w8 new conn to the server
        conn, addr = server.accept()  # store addr of new conn and object that allow us send info back in this conn
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # one thread runs always


print("[STARTING] server is starting...")
start()
