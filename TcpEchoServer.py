#!/usr/bin/python2

import socket

IP = "0.0.0.0"
PORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)

        if data == "close":
            break

        conn.send(data)
    conn.close()
