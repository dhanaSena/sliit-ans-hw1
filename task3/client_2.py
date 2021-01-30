#----- A simple TCP client program in Python using send() function -----

import socket

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Connect to the server

clientSocket.connect(("127.0.0.1",9090));

 
# Receive data from server

dataFromServer = clientSocket.recv(1024);
 

# Print to the console

# Print to the console
print('Client 2 has received %s from the Server' % (dataFromServer.decode()))
