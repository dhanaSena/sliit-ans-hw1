#----- A simple TCP client program in Python using send() function -----

import socket

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Connect to the server

clientSocket.connect(("127.0.0.1",9090));

 

# Send data to server

data = 5;

clientSocket.send(str(data).encode());
 

# Print to the console
print('Client 1 has sent %d to the Server' % (data))
