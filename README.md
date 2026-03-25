# Decentralized Smart Traffic Grid: Edge Computing & Secure Telemetry

## Overview
A decentralized, smart traffic management system that replaces vulnerable centralized servers with Edge Computing. Raspberry Pi edge nodes process simulated vehicle proximity sensors locally to trigger Red/Yellow/Green logic, then securely stream that telemetry over an encrypted Tailscale VPN tunnel using high-speed UDP sockets.

## Engineering Squad
* **Akshay Gudur** 
* **Aditya Sanjay Patil** 
* **Akshath G S** 

## Core Architecture
* **Edge Computing:** Hardware-level traffic logic execution (Raspberry Pi).
* **Zero-Trust Networking:** End-to-end WireGuard encryption via Tailscale (NAT Traversal).
* **Transport Layer:** Custom asynchronous UDP sockets for high-throughput IoT telemetry.
* **Data Serialization:** Lightweight JSON payloads for self-documenting, cross-platform compatibility.

## Hardware Deployment: Headless Edge Node
To maximize the Raspberry Pi's compute resources and emulate a true remote IoT deployment, the edge node was configured in **Headless Mode**. 

We eliminated the need for a physical monitor or peripherals at the intersection. All system administration, code deployment, and script execution were handled entirely via remote shell commands using **SSH (Secure Shell)** routed through the Tailscale Zero-Trust network.

**Deployment Command Sequence:**
```bash
# 1. Securely connect to the Edge Node via Tailscale IP
ssh pi@100.X.X.X

# 2. Execute the traffic logic script remotely
python3 pi_node.py
```

## Phase 1 Stress Test
Successfully load-tested with a 101-node multi-threaded simulation, proving the central Ubuntu server can seamlessly multiplex asynchronous UDP traffic from distributed metropolitan zones without frame drops.