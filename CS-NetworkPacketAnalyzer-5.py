from scapy.all import sniff
from scapy.layers.inet import IP, TCP

def packet_callback(packet):
    # if the packet has ip or tcp layers
    if packet.haslayer(IP):
        ip_src = packet[IP].src  # source IP
        ip_dst = packet[IP].dst  # destination IP
        

        if packet.haslayer(TCP):
            tcp_sport = packet[TCP].sport  # src TCP
            tcp_dport = packet[TCP].dport  # dst TCP
            payload = bytes(packet[TCP].payload) 

            # Display
            print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
            print(f"Source Port: {tcp_sport} -> Destination Port: {tcp_dport}")
            print(f"Payload: {payload}\n")

# filter packets to capture only a certain type
sniff(filter="tcp", prn=packet_callback, store=0)
from scapy.all import sniff
from scapy.layers.inet import IP, TCP

def packet_callback(packet):
    # if the packet has ip or tcp layers
    if packet.haslayer(IP):
        ip_src = packet[IP].src  # source IP
        ip_dst = packet[IP].dst  # destination IP
        

        if packet.haslayer(TCP):
            tcp_sport = packet[TCP].sport  # src TCP
            tcp_dport = packet[TCP].dport  # dst TCP
            payload = bytes(packet[TCP].payload) 

            # Display
            print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
            print(f"Source Port: {tcp_sport} -> Destination Port: {tcp_dport}")
            print(f"Payload: {payload}\n")

# filter packets to capture only a certain type
sniff(filter="tcp", prn=packet_callback, store=0)