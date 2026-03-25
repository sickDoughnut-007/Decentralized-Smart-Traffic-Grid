import socket
import json

# --- CONFIGURATION ---
HOST = "0.0.0.0"  #  Must be 0.0.0.0 to catch Tailscale VPN traffic
PORT = 5005

# Setup UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f" Central Core Server ONLINE.")
print(f"Listening for UDP telemetry on port {PORT} via Tailscale...\n")

while True:
    try:
        # Catch incoming packets
        data, addr = sock.recvfrom(1024)
        
        # Deserialize JSON back into a Python dictionary
        payload = json.loads(data.decode('utf-8'))
        
        # Extract data points
        node = payload.get("intersection_id", "UNKNOWN")
        dist = payload.get("vehicle_distance_cm", 0)
        sig = payload.get("signal_status", "ERR")
        
        # Log the telemetry to the terminal
        print(f" [IP: {addr[0]}] {node} | Dist: {dist}cm | Signal: {sig}")
        
    except KeyboardInterrupt:
        print("\n Server shutting down.")
        break
    except Exception as e:
        print(f" Data Decode Error: {e}")