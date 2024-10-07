import socket

# Step 1: Create a TCP/IP socket | Difference from the server side: serve
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server's IP address and port
server_address = ('localhost', 65432)  # Replace 'server_static_ip' with the actual server IP
client_socket.connect(server_address)

# Step 3: Send data
serial_data = ["Line 1", "Line 2", "Line 3", "Line 4"] # Simulating serial data. In real example this could be the actual serial data stream

for line in serial_data:
    line = "\n" + line 
    client_socket.sendall(line.encode()) # send each line encoded as bytes

# Step 4: Close the connection
client_socket.close()