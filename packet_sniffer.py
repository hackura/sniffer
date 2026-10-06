#!/usr/bin/env python3

"""
Basic Network Packet Sniffer
Author: Karl Seyram Dorpe
for CodeAlpha CYbersecurity Internship Program
"""

from scapy.all import hexdump, sniff, IP, TCP, UDP, ICMP, Raw, hexdump


def packet_callback(packet):
    print("=" * 60)

    # Check if packet contains an IP layer
    if packet.haslayer(IP):
        ip = packet[IP]

        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")

        # Display protocol
        if packet.haslayer(TCP):
            print("Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        else:
            print(f"Protocol Number: {ip.proto}")

        # Display payload if available
        if packet.haslayer(Raw):
            print("Payload (Hex):")
            hexdump(packet[Raw].load)

        print("\nPacket Summary:")
        print(packet.summary())

    print("=" * 60)


def main():
    print("Basic Network Packet Sniffer")
    print("Press Ctrl + C to stop.\n")

    sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        print("Run this program with sudo.")
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")