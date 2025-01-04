from sklearn.datasets import load_iris  # Import the Iris dataset from scikit-learn
import time  # Core Python library for handling time-related tasks
import socket  # Core Python library for networking

# Load the Iris dataset
iris = load_iris()

# Create a socket object with IPv4 addressing and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to all available network interfaces on port 9997
server.bind(("0.0.0.0", 9997))

# Start listening for incoming connections
server.listen()

# Continuously accept and handle incoming connections
while True:
    client, addr = server.accept()  # Accept a new connection
    print("Connection from", addr)  # Print the address of the connected client
    client.send("You are connected!\n".encode())  # Send a connection confirmation message to the client
    client.send(f"{iris.data[:, 0]}\n".encode())  # Send the first feature column of the Iris dataset to the client
    time.sleep(2)  # Pause for 2 seconds
    client.send("You are being disconnected!\n".encode())  # Send a disconnection message to the client
    client.close()  # Close the connection with the client

