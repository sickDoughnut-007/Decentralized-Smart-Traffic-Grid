import socket
import json
import time
import random
import sys

# --- CONFIGURATION ---
# REPLACE THIS with your friend's Tailscale IP address
SERVER_IP = "100.106.129.79" 
SERVER_PORT = 5005

# Get the intersection name from the terminal command
intersection_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown_Intersection"

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"📡 Sensor Node '{intersection_id}' is ONLINE.")
print(f"Transmitting data to Central Server at {SERVER_IP}:{SERVER_PORT}...\n")

while True:
    try:
        # 1. Generate virtual sensor data
        sensor_data = {
            "intersection_id": intersection_id,
            "vehicle_count": random.randint(5, 50),
            "signal_status": random.choice(["RED", "YELLOW", "GREEN"])
        }
        
        # 2. Package into JSON
        payload = json.dumps(sensor_data).encode('utf-8')
        
        # 3. Send via UDP
        sock.sendto(payload, (SERVER_IP, SERVER_PORT))
        print(f"Sent: {sensor_data}")
        
        # 4. Wait 2 seconds before sending the next report
        time.sleep(2)
        
    except KeyboardInterrupt:
        print(f"\n🛑 Shutting down {intersection_id}.")
        break
    except Exception as e:
        print(f"Network Error: {e}")
        time.sleep(0.05) # Wait a bit before retrying if the network drops