#!/usr/bin/env python3
"""
Server that listens for addition requests in the format "Add X Y" and returns the sum.
Example invocation: echo "Add 16 4" | nc localhost 5000
"""
import socket

def handle_client(client_socket):
    """Handle a single client connection."""
    try:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8').strip()
        print(f"Received: {message}")
        
        # Parse the message
        parts = message.split()
        
        if len(parts) == 3 and parts[0].lower() == 'add':
            try:
                num1 = float(parts[1])
                num2 = float(parts[2])
                result = num1 + num2
                response = f"Result: {result}"
            except ValueError:
                response = "Error: Invalid numbers"
        else:
            response = "Error: Invalid format. Use 'Add X Y'"
        
        # Send response back to client
        client_socket.send(response.encode('utf-8'))
        print(f"Sent: {response}")
        
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    # Server configuration
    HOST = '127.0.0.1'  # localhost
    PORT = 5000
    
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind and listen
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    
    print(f"Server listening on {HOST}:{PORT}")
    print("Waiting for connections...")
    
    try:
        while True:
            # Accept client connection
            client_socket, address = server_socket.accept()
            print(f"\nConnection from {address}")
            
            # Handle the client
            handle_client(client_socket)
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
