import socket
import json
import time
import random

# --- CONFIGURATION ---
SERVER_IP = "100.X.X.X"  # REPLACE WITH AKSHATH'S UBUNTU TAILSCALE IP
SERVER_PORT = 5005
INTERSECTION_ID = "Physical_Pi_Node_1"

# --- ANSI COLOR CODES ---
COLOR_GREEN = "\033[42m\033[30m"  # Green background, black text
COLOR_YELLOW = "\033[43m\033[30m" # Yellow background, black text
COLOR_RED = "\033[41m\033[37m"    # Red background, white text
RESET = "\033[0m"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"🚦 Edge Node '{INTERSECTION_ID}' is ONLINE.")
print(f"📡 Transmitting UDP telemetry to {SERVER_IP}:{SERVER_PORT}...\n")

while True:
    try:
        # Hardware Simulation: Generate distance 20cm to 150cm
        simulated_distance = random.randint(20, 150) 
        
        # Local Edge Logic: 3-State Traffic Grid
        if simulated_distance < 60:
            signal = "GREEN"
            visual = f"{COLOR_GREEN} [  GREEN LIGHT  ] {RESET}"
        elif 60 <= simulated_distance < 100:
            signal = "YELLOW"
            visual = f"{COLOR_YELLOW} [ YELLOW LIGHT  ] {RESET}"
        else:
            signal = "RED"
            visual = f"{COLOR_RED} [   RED LIGHT   ] {RESET}"

        # Package the JSON payload
        sensor_data = {
            "intersection_id": INTERSECTION_ID,
            "vehicle_distance_cm": simulated_distance,
            "signal_status": signal
        }
        
        payload = json.dumps(sensor_data).encode('utf-8')
        
        # Fire the UDP packet across the Tailscale tunnel
        sock.sendto(payload, (SERVER_IP, SERVER_PORT))
        
        # Print the stunning visual to the terminal
        print(f"Dist: {simulated_distance:3}cm | Signal: {visual} | Transmitting...")
        
        time.sleep(1)
        
    except KeyboardInterrupt:
        print("\nShutting down Edge Node.")
        break
    except Exception as e:
        print(f"Network Error: {e}")
        time.sleep(2)