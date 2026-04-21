import socket
import json

# --- CONFIGURATION ---
# Binds to all interfaces (Wi-Fi, Ethernet, Tailscale)
UDP_IP = "0.0.0.0"  
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("=====================================================")
print("🌐 CENTRAL COMMAND ONLINE: Phase 2 Hybrid Architecture")
print(f"🎧 Listening for 4-Way UDP telemetry on port {UDP_PORT}...")
print("=====================================================\n")

while True:
    try:
        # Receive raw UDP datagram (buffer size 1024 bytes)
        data, addr = sock.recvfrom(1024) 
        
        # Decode the JSON payload
        payload = json.loads(data.decode('utf-8'))
        
        # Extract the nested Phase 2 data
        node_id = payload.get("intersection_id", "UNKNOWN")
        mutex = payload.get("active_mutex_state", "N/A")
        
        sensors = payload.get("sensors_cm", {})
        n, s, e, w = sensors.get('N', 0), sensors.get('S', 0), sensors.get('E', 0), sensors.get('W', 0)
        
        signals = payload.get("signals", {})
        ns_axis = signals.get('NS_Axis', 'ERR')
        ew_axis = signals.get('EW_Axis', 'ERR')

        # Format and print the high-speed data stream
        print(f"[{node_id}] Mutex: {mutex:<9} | N:{n:3} S:{s:3} E:{e:3} W:{w:3} | NS:{ns_axis:<6} EW:{ew_axis:<6}")

    except json.JSONDecodeError:
        print(f"⚠️ Dropped malformed packet from {addr}")
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Central Command.")
        break
    except Exception as e:
        print(f"Server Error: {e}")