#----- A simple TCP based server program in Python using send() function -----



import socket



# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);



# Bind and listen

serverSocket.bind(("127.0.0.1",9090));

# configure how many client the server can listen simultaneously
serverSocket.listen(2)

count = 0;
s = 0;

# Accept connections

while(True):

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));

    if count == 0:
        dataFromClient = clientConnected.recv(1024)
        temp_str = dataFromClient.decode();
        #set the client1 send data
        s = int(temp_str)
        clientConnected.close();
    else :
        # Decrement Integer
        s -= 1;
        # Send some data back to the client
        clientConnected.send(str(s).encode());
        clientConnected.close();
        break;

    count += 1
