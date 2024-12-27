# client_server

The entire process can be broken down into following steps:
TCP Server – 
1. using create(), Create TCP socket.
2. using bind(), Bind the socket to server address.
3. using listen(), put the server socket in a passive mode, where it waits for the client to approach the server to make a connection
4. using accept(), At this point, connection is established between client and server, and they are ready to transfer data.
5. Go back to Step 3.

TCP Client – 
6. Create TCP socket.
7. connect newly created client socket to server.
