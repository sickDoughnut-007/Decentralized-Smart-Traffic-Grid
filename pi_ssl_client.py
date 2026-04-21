import socket
import ssl

# --- CONFIGURATION ---
# 🚨 REPLACE WITH AKSHATH'S LOCAL WI-FI IP
SERVER_IP = "192.168.X.X"  
PORT = 8443

# 1. Create the SSL Context for a Client
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# 2. Bypass strict verifications (required for Self-Signed certs on local networks)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 3. Create raw socket and wrap it
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(raw_socket, server_hostname=SERVER_IP)

print(f"Attempting to establish secure connection to {SERVER_IP}:{PORT}...")

try:
    secure_socket.connect((SERVER_IP, PORT))
    print("===================================================")
    print("🔒 TLS HANDSHAKE SUCCESSFUL.")
    print("Listening for secure override commands...")
    print("===================================================\n")

    while True:
        data = secure_socket.recv(1024)
        if not data:
            print("Connection closed by central server.")
            break
            
        command = data.decode('utf-8')
        print(f"🚨 [CRITICAL OVERRIDE RECEIVED] Executing: {command}")

except Exception as e:
    print(f"Connection Failed: {e}")
finally:
    secure_socket.close()