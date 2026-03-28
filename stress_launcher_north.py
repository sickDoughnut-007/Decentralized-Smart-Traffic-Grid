import socket
import json
import time
import random
import threading

# --- CONFIGURATION ---
SERVER_IP = "100.X.X.X"  
SERVER_PORT = 5005
NUM_NODES = 50           # Number of virtual intersections per laptop
GRID_ZONE = "North_City_Grid" 
print(f" INITIATING METROPOLITAN STRESS TEST: {NUM_NODES} VIRTUAL NODES")
print(f" Target Zone: {GRID_ZONE}")
print(f" Target Server: {SERVER_IP}:{SERVER_PORT}\n")

def simulate_node(node_id):
    # Give each virtual node its own UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    intersection_name = f"{GRID_ZONE}_{node_id}"
    
    while True:
        try:
            # Simulate real-world chaotic traffic distances
            distance = random.randint(20, 150)
            
            # Matched 3-State Edge Logic
            if distance < 60:
                signal = "GREEN"
            elif 60 <= distance < 100:
                signal = "YELLOW"
            else:
                signal = "RED"
            
            payload = {
                "intersection_id": intersection_name,
                "vehicle_distance_cm": distance,
                "signal_status": signal
            }
            
            # Fire the UDP packet
            sock.sendto(json.dumps(payload).encode('utf-8'), (SERVER_IP, SERVER_PORT))
            
            # Sleep for a random fraction of a second to simulate asynchronous traffic
            time.sleep(random.uniform(0.2, 1.5)) 
            
        except Exception as e:
            pass # Ignore dropouts to keep the stress test running

# Spawn 50 simultaneous threads, one for each virtual node
for i in range(1, NUM_NODES + 1):
    threading.Thread(target=simulate_node, args=(i,), daemon=True).start()

# Keep the main script alive while the background threads run
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n Stress Test Aborted.")