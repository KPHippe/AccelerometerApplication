import subprocess
import socket
import json
import numpy as np
#Creates a TCP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#We bind the socket to port 9999
s.bind(('', 9999))
#We allow 5 connections to be in the queue, we are waiting for 1 or more (up to 5) connections
s.listen(5)

while True:
    #We accept the incoming connection, wait for a connection if it doesn't come immediately
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    while True:
        x = subprocess.run(['cat', '/sys/kernel/accel/x'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)
        y = subprocess.run(['cat', '/sys/kernel/accel/y'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)
        z = subprocess.run(['cat', '/sys/kernel/accel/z'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)


        msg = [("x", x.stdout), ("y", y.stdout), ("z", z.stdout)]

        msg = json.JSONEncoder().encode(msg)


        clientsocket.send(bytes(msg, "utf-8"))


    clientsocket.close()
    print(f"Connection from {address} has been closed")