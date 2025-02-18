# client.py
import socket
import sys

def start_client(host, port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server's address and port
    server_address = (host, port)
    print(f"Connecting to {host} port {port}")
    
    try:
        client_socket.connect(server_address)
        print("Connected to server! Type 'quit' to exit.")
        
        while True:
            # Get message from user
            message = input("Enter message: ")
            
            # Check if user wants to quit
            if message.lower() == 'quit':
                break
                
            # Send data
            print(f"Sending: {message}")
            client_socket.sendall(message.encode())
            
            # Look for the response
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}\n")
            
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running and the IP address is correct.")
    except socket.gaierror:
        print("Address error. Make sure the IP address is correct.")
    finally:
        # Clean up
        print("Closing connection")
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <port>")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    start_client(host, port)