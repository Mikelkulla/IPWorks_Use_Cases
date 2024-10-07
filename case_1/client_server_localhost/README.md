# Case 1: TCP Client-Server for Binary Data Transfer
## Overview
This project implements a TCP client-server application in Python that transfers binary data over a local network. The client reads data from a specified source (simulated here as simple text) and sends it to the server, which listens for incoming connections and processes the received data.

## Components
Server: A TCP server that accepts incoming connections and receives data, printing it to the console.
Client: A TCP client that connects to the server and sends data.

## Technologies Used
Python (standard libraries)

## Installation
No additional libraries are required for this implementation. You only need Python installed on your machine.

## Usage
### Server
Create a file named server.py
### Client
Create a file named client.py 

## How It Works
The server listens for incoming TCP connections on localhost:65432.
The client connects to the server and sends five lines of data.
The server receives the data and prints it to the console.

## Testing
Start the server by running server.py.
In a separate terminal, run the client script client.py.
Observe the server console to see the received data.

## Challenges
Managing proper connections and ensuring data was sent and received without loss.
Handling potential connection errors gracefully.

## Conclusion
This project demonstrates a simple implementation of a TCP client-server model in Python for transferring binary data over a local network. It serves as a foundation for understanding network programming concepts in Python.
