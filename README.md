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

## Phase 1 Stress Test
Successfully load-tested with a 101-node multi-threaded simulation, proving the central Ubuntu server can seamlessly multiplex asynchronous UDP traffic from distributed metropolitan zones without frame drops.