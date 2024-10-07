# Case 1: TCP Client-Server for Real-Time Data Transfer
## Overview
This project implements a TCP client-server application in Python designed for real-time data transfer. The client reads data from a connected serial device (e.g., sensors, microcontrollers) and sends this data to a TCP server, which listens for incoming connections and processes the received data.

## Components
Server: A TCP server that accepts incoming connections from clients, receives data, and prints it to the console for monitoring.
Client: A TCP client that connects to the server, reads data from a specified serial port, and sends it continuously.

## Technologies Used
Python (standard libraries)
PySerial library for serial communication

## Installation
####Install the pyserial library to manage serial connections:
pip install pyserial

## Usage
### Server
Create a file named server.py 
Run the server script to start listening for incoming connections
python server.py
###Client
1. Create a file named client.py 
2. Update the client code with the correct serial port and server IP address.
3. Run the client script to connect to the server and start sending real-time data:
python client.py

## How It Works
The server listens for incoming TCP connections on 0.0.0.0:65432, allowing connections from any network interface.
The client reads data from a connected serial device, processes it, and sends it to the server over TCP.
The server receives and prints the data to the console, allowing for real-time monitoring.

## Testing
Start the server by running server.py.
Connect your serial device and run the client script client.py.
Monitor the server's console output to observe the real-time data being sent from the client.

## Challenges
Configuring the correct serial port settings and ensuring the device was connected properly.
Handling potential network issues, such as firewall settings that could block incoming connections.

## Conclusion
This project demonstrates a practical implementation of a TCP client-server model in Python for transferring real-time data from a serial device over a network. It serves as a foundation for more complex data acquisition and monitoring systems.