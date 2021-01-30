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
s = 0.0;

# Accept connections

while(True):

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));

    if count == 0:
        dataFromClient = clientConnected.recv(1024)
        temp_str = dataFromClient.decode();
        print("Received the float from Client 1 : %s"%(temp_str))
        #set the client1 send data
        s = float(temp_str)
        clientConnected.close();
    else :
        # Obtain expo from the float
        result = pow(s,1.5)
        print("Sending the float to Client 2 : %8.2f"%(result))
        # Send some data back to the client
        clientConnected.send(str(result).encode());
        clientConnected.close();
        break;

    count += 1
