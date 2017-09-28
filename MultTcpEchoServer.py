#!/usr/bin/env python

import socket
from multiprocessing import Process, freeze_support
import os

def worker(sock):
    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)

                if data == "close":
                    break

                conn.send(data)

if __name__ == "__main__":

    if os.name == "nt":
        freeze_support()

    IP = "0.0.0.0"
    PORT = 2222
    NUM_OF_PROCS = 10

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(10)

    procs = []

    for _ in xrange(NUM_OF_PROCS):
        proc = Process(target = worker, args = (sock,))
        procs.append(proc)

    for pr in procs:
        pr.start()

    for pr in procs:
        pr.join()

