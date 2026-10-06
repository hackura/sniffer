<div align="center">

# Basic Network Packet Sniffer

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Packet%20Analysis-2E8B57)
![License](https://img.shields.io/badge/license-educational-lightgrey)

**A basic command-line Network packet sniffer built with Python and Scapy.**

</div>

## Overview

`packet_sniffer.py` captures network packets and displays useful information about IPv4 traffic, including:

- Source and destination IP addresses
- TCP, UDP, and ICMP protocols
- Source and destination ports for TCP and UDP
- Raw payload data in hexadecimal format
- A Scapy packet summary

> Use this tool only on networks and devices that you own or are explicitly authorized to monitor.

## How it works

![Packet sniffing workflow](/result.png)

The program listens for packets, passes each packet to `packet_callback`, then prints protocol and payload details when available.

## Requirements

- Python 3.8 or newer
- Scapy
- Administrator/root privileges for packet capture
- Virtual environment enabled with 
```bash
python3 -m venv .venv
```

Install Scapy:

```bash
python3 -m pip install scapy
```
OR

```bash
pip install -r requirements.txt
```
## Usage

From the project directory, run:

```bash
sudo python3 packet_sniffer.py
```

Press **Ctrl+C** to stop capturing packets.

Example output:

```text
============================================================
Source IP      : 192.168.1.10
Destination IP : 142.250.72.14
Protocol       : TCP
Source Port    : 51524
Destination Port: 443
Packet Summary:
IP / TCP 192.168.1.10:51524 > 142.250.72.14:https S
============================================================
```

## Code structure

| Function | Description |
| --- | --- |
| `packet_callback(packet)` | Formats and displays captured packet details. |
| `main()` | Starts packet capture with Scapy's `sniff()` function. |

## Troubleshooting

If packet capture fails with a permissions error, run the script with `sudo` or use an account with the required capture privileges.

## Author

**Karl Seyram Dorpe**

## Disclaimer

This project is intended for educational and authorized network diagnostics only. Do not capture or inspect traffic without permission.
