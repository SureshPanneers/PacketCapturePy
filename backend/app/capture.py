import os, time, random
try:
    from scapy.all import sniff, rdpcap, IP, TCP, UDP, Raw, Ether
    SCAPY_AVAILABLE = True
except Exception:
    SCAPY_AVAILABLE = False

class PacketCapture:
    def __init__(self, use_real=False):
        self.use_real = use_real and SCAPY_AVAILABLE
        self.last_packets = []  # will store either scapy Packet objects or dicts (for mock)

    def capture(self, count=5, use_real=None, timeout=10):
        \"\"\"Return a list of captured packets. If scapy+permissions absent, falls back to mock packets.\"\"\"
        if use_real is None:
            use_real = self.use_real
        if use_real and SCAPY_AVAILABLE:
            # perform real sniffing (may require root)
            pkts = sniff(count=count, timeout=timeout)
            self.last_packets.extend(pkts)
            return pkts
        else:
            # mock packets
            pkts = [self._generate_mock_packet(i) for i in range(count)]
            self.last_packets.extend(pkts)
            return pkts

    def _generate_mock_packet(self, idx=0):
        # simple synthetic packet-like dict for UI and tests
        proto = random.choice(['TCP','UDP','ICMP','HTTP','DNS','ARP'])
        pkt = {
            'timestamp': time.time(),
            'src_ip': f\"192.168.1.{random.randint(2,250)}\",
            'dst_ip': f\"10.0.0.{random.randint(2,250)}\",
            'protocol': proto,
            'src_port': random.randint(1024,65535) if proto in ('TCP','UDP','HTTP','DNS') else None,
            'dst_port': random.choice([80,443,53,22,8080, None]) if proto in ('TCP','UDP','HTTP','DNS') else None,
            'length': random.randint(60,1500),
            'raw': None,
        }
        return pkt

    def get_last_packets(self, limit=100):
        return self.last_packets[-limit:]

    def parse_pcap_file(self, filename):
        if not SCAPY_AVAILABLE:
            return None
        try:
            pkts = rdpcap(filename)
            # convert to list; keep scapy Packet objects
            return list(pkts)
        except Exception as e:
            print('error reading pcap', e)
            return None
