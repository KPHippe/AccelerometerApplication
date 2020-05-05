import socket
import sys
import json
#Change this address to the IP address of the computer that is running the server

RPIADDR= '10.0.0.112'
LOCAL = '127.0.0.1'
#creates a TCP socket, we might end up using TCP, but we will see about the future
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Using the socket object we created, connect to the server IP at the given port number
s.connect((RPIADDR,9999))


while True:
    recMessage = s.recv(256).decode("utf-8")

    #if we actually received something from the server, print it out and continue
    if(len(recMessage) > 0):
        recMessage = recMessage.split()
        x = int(recMessage[0])
        y = int(recMessage[1])
        z = int(recMessage[2])
        print(f"x: {x}\ty: {y}\tz: {z}")
        # print(f"received '{recMessage}' from server")
    #Else, something went wrong
    #TCP creates a 'tunnell' so if you don't get anything back that means your connection failed
    #if it does fail, you have to close everything and restart
    else:
        print(f"Error receiving, closing")
        sys.exit()