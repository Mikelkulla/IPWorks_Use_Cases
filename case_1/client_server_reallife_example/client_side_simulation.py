import socket
import time

# Step 1: Skip

# Step 2: Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step3: Connect to the server's localhost address and port
server_address = ('localhost', 65432) # Using localhost for local testing
client_socket.connect(server_address)

# Step4: Continuously send simulated serial data to the server
try:
    while True:
        simulated_data = "Line" # Simulating serial data
        print(f'Sending: {simulated_data}')
        client_socket.sendall(simulated_data.encode()) # Send the data to the server
        time.sleep(0.1) # Wait 1 second before sending the next line
except KeyboardInterrupt:
    print("Client stopped by user.")