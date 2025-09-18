from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, Raw

app = FastAPI(title="Network Packet Analysis API")

# Allow React frontend (port 3000) to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins in dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Root endpoint to verify API is running."""
    return {"message": "Welcome to the Network Packet Analysis API"}


def capture_real_packets(count: int):
    """Capture real packets from the network using Scapy with protocol classification and payload preview."""
    packets = []

    def process_packet(pkt):
        if IP in pkt:
            proto = "OTHER"
            payload_preview = None

            if ICMP in pkt:
                proto = "ICMP"
            elif TCP in pkt:
                if pkt[TCP].sport == 80 or pkt[TCP].dport == 80:
                    proto = "HTTP"
                else:
                    proto = "TCP"
            elif UDP in pkt:
                if pkt[UDP].sport == 53 or pkt[UDP].dport == 53:
                    proto = "DNS"
                else:
                    proto = "UDP"

            # Extract raw payload if present
            if Raw in pkt:
                raw_bytes = bytes(pkt[Raw].load)
                payload_preview = raw_bytes[:50].decode("utf-8", errors="replace")

            packet_info = {
                "src": pkt[IP].src,
                "dst": pkt[IP].dst,
                "protocol": proto,
                "payload": payload_preview,
            }
            packets.append(packet_info)

    sniff(count=count, prn=process_packet, store=False)
    return packets


@app.get("/capture")
def capture_packets(count: Optional[int] = 10, mock: bool = True):
    """
    Capture live packets (or mock packets) and return parsed JSON structures.

    Args:
        count (int): Number of packets to capture (default: 10).
        mock (bool): If True, return mock packets instead of live capture.

    Returns:
        dict: Captured or mock packet data.
    """
    if mock:
        packets = [
            {"id": i, "src": "192.168.0.1", "dst": "192.168.0.2", "protocol": "TCP", "payload": "Mock payload"}
            for i in range(count)
        ]
    else:
        real_packets = capture_real_packets(count)
        packets = [{"id": i, **pkt} for i, pkt in enumerate(real_packets)]

    return {"packets": packets}


@app.get("/stats")
def get_stats(count: Optional[int] = 20):
    """
    Capture packets and return statistics of TCP, UDP, ICMP, DNS, HTTP, and Others.
    """
    real_packets = capture_real_packets(count)

    stats = {
        "total_packets": len(real_packets),
        "tcp_packets": 0,
        "udp_packets": 0,
        "icmp_packets": 0,
        "dns_packets": 0,
        "http_packets": 0,
        "other_packets": 0,
    }

    for pkt in real_packets:
        if pkt["protocol"] == "TCP":
            stats["tcp_packets"] += 1
        elif pkt["protocol"] == "UDP":
            stats["udp_packets"] += 1
        elif pkt["protocol"] == "ICMP":
            stats["icmp_packets"] += 1
        elif pkt["protocol"] == "DNS":
            stats["dns_packets"] += 1
        elif pkt["protocol"] == "HTTP":
            stats["http_packets"] += 1
        else:
            stats["other_packets"] += 1

    return {"stats": stats}
