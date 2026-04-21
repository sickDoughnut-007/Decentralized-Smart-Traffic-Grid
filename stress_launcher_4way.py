import socket
import json
import time
import random

# --- CONFIGURATION ---
# 🚨 REPLACE WITH AKSHATH'S LOCAL WI-FI IP (e.g., 192.168.1.X)
SERVER_IP = "100.106.129.79"  
SERVER_PORT = 5005

# 🚨 ADITYA: Change this on PC 2 to "Sector_Beta"
GRID_NAME = "Sector_Alpha" 
NUM_NODES = 50

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"🚀 Launching 4-Way Swarm Stress Test for {GRID_NAME} ({NUM_NODES} nodes)...")
print(f"📡 Targeting {SERVER_IP}:{SERVER_PORT} over Local Wi-Fi\n")

# Valid Phase 2 Mutex States (Guarantees no virtual car crashes)
MUTEX_STATES = [
    ('NS_GREEN', 'GREEN', 'RED'),
    ('NS_YELLOW', 'YELLOW', 'RED'),
    ('EW_GREEN', 'RED', 'GREEN'),
    ('EW_YELLOW', 'RED', 'YELLOW')
]

try:
    while True:
        # Rapidly loop through and generate 50 unique virtual nodes
        for i in range(1, NUM_NODES + 1):
            node_id = f"{GRID_NAME}_Node_{i:02d}"
            
            # Pick a valid, safe Mutex state for the virtual intersection
            state, ns_light, ew_light = random.choice(MUTEX_STATES)
            
            # Package the complex Phase 2 payload
            sensor_data = {
                "intersection_id": node_id,
                "sensors_cm": {
                    "N": random.randint(20, 150), 
                    "S": random.randint(20, 150), 
                    "E": random.randint(20, 150), 
                    "W": random.randint(20, 150)
                },
                "signals": {"NS_Axis": ns_light, "EW_Axis": ew_light},
                "active_mutex_state": state
            }
            
            payload = json.dumps(sensor_data).encode('utf-8')
            
            # Fire the UDP packet
            sock.sendto(payload, (SERVER_IP, SERVER_PORT))
            
        # A 50-millisecond sleep prevents the local Wi-Fi router from dropping packets
        time.sleep(0.05) 
            
except KeyboardInterrupt:
    print(f"\n🛑 {GRID_NAME} Stress Test Terminated.")