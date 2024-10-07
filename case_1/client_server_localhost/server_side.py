import socket

# Step 1: Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET specifies the address family as IPv4 | SOCK_STREAM means we are using a stream socket which uses TCP

# Step 2: Bind the socket to the server's IP address and a port
server_address = ('0.0.0.0', 65432)  # 0.0.0.0 means it will listen on all available network interfaces
server_socket.bind(server_address)

# Step 3: Listen for incoming connections
server_socket.listen(1)  # The '1' means the server will queue up 1 connection request
print("Server is listening for connections...")

# Step 4: Wait for a connection
"""
server calls accept() which blocks the program until a client tries to connect.
once a client connects, accept() returns a new socket object (connection) and 
the address of the client (client_address).
The connection socket is used to communicate with the connected client. You now have a dedicated communication channel between the server and the particular client
"""
connection, client_address = server_socket.accept() 
print(f'Connected to: {client_address}')

# Step5: Receive data in a loop
while True: # This loop continues until the client stops sending data
    data = connection.recv(1024) # Buffer size of 1024 bytes
    if data:
        print(f'Received: {data.decode()} \n') # The data is in bytes so we decode it to concvert to a string 
    else:
        break

# Step 6: Clean up (close the connection)
connection.close()
server_socket.close()