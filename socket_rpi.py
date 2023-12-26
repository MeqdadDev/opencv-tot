import socket

RASPBERRY_PI_IP = '192.168.1.10'
PORT = 3000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the Raspberry Pi's IP and port
server_socket.bind((RASPBERRY_PI_IP, PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for incoming connections...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")
while True:
    # Receive message from the client (PC)
    message = client_socket.recv(1024).decode()
    print(f"Received message from PC: {message}")
    # If the received message is 'exit', close the connection
    if message.lower() == 'exit':
        break
    # Send a response back to the client (PC)
    response = input("Enter your response: ")
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()
