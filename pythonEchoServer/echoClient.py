import socket
import sys

#Change this address to the IP address of the computer that is running the server

RPIADDR= '10.0.0.112'
LOCAL = '127.0.0.1'
#creates a TCP socket, we might end up using TCP, but we will see about the future
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Using the socket object we created, connect to the server IP at the given port number
s.connect((LOCAL, 9999))


while True:
    #Gets the user input
    sendMessage = input("Message to send to server: ")
    #Have to send datta as a bytestream, so encode the message we input into a
    #bytestream with a unicode tag, so the server can decipher it later
    s.send(bytes(sendMessage, "utf-8"))
    #Wait for the server to send back the message, decode it
    recMessage = s.recv(256).decode("utf-8")

    #if we actually received something from the server, print it out and continue
    if(len(recMessage) > 0):
        print(f"received '{recMessage}' from server")
    #Else, something went wrong
    #TCP creates a 'tunnell' so if you don't get anything back that means your connection failed
    #if it does fail, you have to close everything and restart
    else:
        print(f"Error receiving, closing")
        sys.exit()
