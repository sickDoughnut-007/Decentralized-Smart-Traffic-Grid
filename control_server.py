import socket
import ssl

# --- CONFIGURATION ---
HOST = "0.0.0.0" 
PORT = 8443  # Standard port for secure alternate traffic

# 1. Create a standard TCP Socket
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw_socket.bind((HOST, PORT))
raw_socket.listen(1)

# 2. Create the SSL Context (Load the Certificates)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# 3. Wrap the socket in military-grade TLS encryption
secure_socket = context.wrap_socket(raw_socket, server_side=True)

print("===================================================")
print(f"🔒 SECURE CONTROL PLANE ONLINE (Port {PORT})")
print("Waiting for Edge Node to authenticate...")
print("===================================================\n")

try:
    # Accept the connection from the Pi
    client_conn, client_addr = secure_socket.accept()
    print(f"✅ Secure connection established with {client_addr}")
    
    while True:
        # Ask the admin to type a command
        command = input("Enter Override Command (e.g., FORCE_NS_GREEN) or 'exit': ")
        
        if command.lower() == 'exit':
            break
            
        # Send the encrypted command over the wire
        client_conn.send(command.encode('utf-8'))
        print("Command transmitted securely.")

except Exception as e:
    print(f"SSL Server Error: {e}")
finally:
    secure_socket.close()