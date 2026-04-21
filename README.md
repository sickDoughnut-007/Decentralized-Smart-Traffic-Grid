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

### Hardware Deployment: Headless Edge Node

To maximize the Raspberry Pi's compute resources and emulate a true remote IoT deployment, the edge node was configured in **Headless Mode**. 

We eliminated the need for a physical monitor, keyboard, or peripherals at the intersection. All system administration, code deployment, and multi-threaded script execution were handled entirely via remote shell commands using **SSH (Secure Shell)** over a localized high-speed network.

**Deployment Command Sequence:**
Because the Phase 2 architecture utilizes a Hybrid Control Plane, the edge node requires dual-process execution to handle both telemetry and secure administrative overrides simultaneously.

```bash
# 1. Securely connect to the Edge Node via local network mDNS
ssh akshay@akshayraspberrypi.local

# 2. [Terminal 1] Initialize the UDP Data Plane (4-Way Mutex Logic)
python3 pi_node_4way.py

# 3. [Terminal 2] Initialize the TCP+SSL Control Plane (Encrypted Overrides)
python3 pi_ssl_client.py
```

## Phase 2: Enterprise Hybrid Architecture
To scale the network for a true smart-city deployment, the system was upgraded to a **Hybrid Control Plane** featuring localized state machines, asymmetric encryption, and massive swarm handling.

* **4-Way Mutex State Machine (`pi_node_4way.py`):** Replaced the basic reactive loop with a non-blocking Mutex lock. The edge node simulates a full 4-way intersection (North/South vs. East/West), guaranteeing safe yellow-light transitions and strictly preventing cross-traffic collisions via mutual exclusion.
* **The Hybrid Network (UDP + TCP/SSL):** * **The Data Plane (UDP):** A high-speed, fire-and-forget UDP socket continuously streams complex, nested JSON sensor arrays to the central server.
  * **The Control Plane (TCP + TLS):** A secondary, highly secure TCP socket wrapped in an **RSA-4096 SSL certificate**. This allows the central server to send guaranteed, encrypted override commands (e.g., `FORCE_NS_GREEN` for emergency vehicles) that dynamically hijack the local Mutex lock.
* **Swarm Benchmarking (`stress_launcher_4way.py`):** Developed a multi-threaded swarm launcher to evaluate server load. The system successfully multiplexed over 100 virtual intersections across discrete namespaces (`Sector_Alpha`, `Sector_Beta`), executing thousands of non-colliding Mutex payloads without dropping a single UDP frame.