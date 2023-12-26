import socket

# PC IP and port to connect to the Raspberry Pi server
RASPBERRY_PI_IP = '192.168.1.10'
PORT = 3000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Raspberry Pi server
client_socket.connect((RASPBERRY_PI_IP, PORT))
print("Connected to Raspberry Pi")

while True:
    # Send a message to the Raspberry Pi server
    message = input("Enter your message: ")
    client_socket.send(message.encode())

    # If the sent message is 'exit', break the loop
    if message.lower() == 'exit':
        break

    # Receive the response from the server (Raspberry Pi)
    response = client_socket.recv(1024).decode()
    print(f"Received response from Raspberry Pi: {response}")

# Close the socket
client_socket.close()
