import socket
import serial
import time

# Step 1: Set up the serial port
# Replace 'COM3' with the actual port your serial device is connected to
ser = serial.Serial('COM3', 9600, timeout=1)  # Adjust the port and baud rate as needed

# Step 2: Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 3: Connect to the server's localhost address and port
server_address = ('localhost', 65432)  # Using localhost for local testing, Replace with the actual server IP and Port
client_socket.connect(server_address)

# Step 4: Continuously read from the serial port and send data to the server
try:
    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting in the serial buffer
            serial_line = ser.readline().decode('utf-8').strip()  # Read a line from the serial port
            print(f"Read from serial: {serial_line}")  # Print the read line
            client_socket.sendall(serial_line.encode())  # Send the data to the server
        # Sleep briefly to avoid overwhelming the CPU
        time.sleep(0.1)  # Adjust this values as necessary for your application

except KeyboardInterrupt:
    print("Client stopped by user.")

finally:
    client_socket.close()
    ser.close()