import socket


#Creates a TCP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#We bind the socket to port 9999
s.bind((socket.gethostname(), 9999))
#We allow 5 connections to be in the queue, we are waiting for 1 or more (up to 5) connections
s.listen(5)

while True:
    #We accept the incoming connection, wait for a connection if it doesn't come immediately
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    
    while True:
        message = ''
        #We wait for a message to come from the client and decode it
        message = clientsocket.recv(256).decode("utf-8")
        #if the length of the message is < 0, an error occured, we break and close the connection, see the client for why
        if len(message) <= 0:
            break
        print(f"Message from client: {message}")
        #we just send the info back to the client
        clientsocket.send(bytes(message,"utf-8"))

    #Close the socket, this is if there is an error
    clientsocket.close()
    print(f"Connection from {address} has been closed.")