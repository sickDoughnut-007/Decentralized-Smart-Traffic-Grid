import socket
import json
import time
import random

# --- CONFIGURATION ---
SERVER_IP = "192.168.X.X"  
SERVER_PORT = 5005
NODE_ID = "Pi_Hardware_Node"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mutex States
states = ['NS_GREEN', 'NS_YELLOW', 'EW_GREEN', 'EW_YELLOW']
current_state_idx = 0

print("=====================================================")
print(f"🚦 EDGE NODE ONLINE: {NODE_ID}")
print(f"📡 Streaming UDP telemetry to {SERVER_IP}:{SERVER_PORT}")
print("=====================================================\n")

try:
    while True:
        state = states[current_state_idx]
        
        # Determine signals based on active Mutex state
        ns_axis = "GREEN" if state == 'NS_GREEN' else ("YELLOW" if state == 'NS_YELLOW' else "RED")
        ew_axis = "GREEN" if state == 'EW_GREEN' else ("YELLOW" if state == 'EW_YELLOW' else "RED")

        sensor_data = {
            "intersection_id": NODE_ID,
            "sensors_cm": {
                "N": random.randint(20, 150), 
                "S": random.randint(20, 150), 
                "E": random.randint(20, 150), 
                "W": random.randint(20, 150)
            },
            "signals": {"NS_Axis": ns_axis, "EW_Axis": ew_axis},
            "active_mutex_state": state
        }
        
        payload = json.dumps(sensor_data).encode('utf-8')
        sock.sendto(payload, (SERVER_IP, SERVER_PORT))
        
        print(f"[{state:<9}] Sensors (N:{sensor_data['sensors_cm']['N']:3} S:{sensor_data['sensors_cm']['S']:3} E:{sensor_data['sensors_cm']['E']:3} W:{sensor_data['sensors_cm']['W']:3}) | NS:{ns_axis:<6} EW:{ew_axis:<6}")
        
        # Simulate Mutex handoff every 3 loops for the physical node
        if random.random() > 0.6:
            current_state_idx = (current_state_idx + 1) % len(states)
            
        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Edge Node Shutting Down.")