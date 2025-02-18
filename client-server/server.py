# server.py
import socket
import sys

def start_server(port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow address reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to all available interfaces
    server_address = ('0.0.0.0', port)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    # Print all available IP addresses
    hostname = socket.gethostname()
    addresses = socket.gethostbyname_ex(hostname)[2]
    print(f"Server is listening on port {port}")
    print("Available IP addresses:")
    for ip in addresses:
        print(f"  {ip}")
    
    while True:
        # Wait for a connection
        print("\nWaiting for a connection...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Connection from {client_address}")
            
            # Receive the data in small chunks and echo it back
            while True:
                data = connection.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
                    connection.sendall(data)
                else:
                    break
                
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
    
    port = int(sys.argv[1])
    start_server(port)
