#!/usr/bin/env python3
"""
Client that sends addition requests to the server in the format "Add X Y".
"""
import socket

def main():
    # Server configuration
    HOST = '127.0.0.1'  # localhost
    PORT = 5000
    
    # Get numbers from user
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Create message
    message = f"Add {num1} {num2}"
    
    try:
        # Create socket and connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        # Send message
        print(f"\nSending: {message}")
        client_socket.send(message.encode('utf-8'))
        
        # Receive response
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
        
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
