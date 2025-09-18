try:
    from scapy.all import IP, TCP, UDP, DNSQR, UDP, DNS, Raw, Ether
    SCAPY_AVAILABLE = True
except Exception:
    SCAPY_AVAILABLE = False

def parse_packet_dict(pkt):
    \"\"\"Take either a mock dict (from PacketCapture._generate_mock_packet) or a scapy Packet and return a serializable dict.\"\"\"
    if isinstance(pkt, dict):
        return {
            'timestamp': pkt.get('timestamp'),
            'src_ip': pkt.get('src_ip'),
            'dst_ip': pkt.get('dst_ip'),
            'protocol': pkt.get('protocol'),
            'src_port': pkt.get('src_port'),
            'dst_port': pkt.get('dst_port'),
            'length': pkt.get('length'),
            'info': 'mock packet'
        }
    if not SCAPY_AVAILABLE:
        return {'timestamp': None, 'src_ip': None, 'dst_ip': None, 'protocol': 'UNKNOWN', 'src_port': None, 'dst_port': None, 'length': None, 'info': 'scapy not available'}

    # scapy Packet parsing
    info = ''
    proto = 'UNKNOWN'
    src_ip = None
    dst_ip = None
    src_port = None
    dst_port = None

    try:
        if pkt.haslayer(IP):
            ip = pkt.getlayer(IP)
            src_ip = ip.src
            dst_ip = ip.dst
            if pkt.haslayer(TCP):
                tcp = pkt.getlayer(TCP)
                proto = 'TCP'
                src_port = tcp.sport
                dst_port = tcp.dport
                if pkt.haslayer(Raw):
                    raw = pkt.getlayer(Raw).load
                    info = raw[:100].hex()
            elif pkt.haslayer(UDP):
                udp = pkt.getlayer(UDP)
                proto = 'UDP'
                src_port = udp.sport
                dst_port = udp.dport
            else:
                proto = ip.proto
        elif pkt.haslayer(Ether):
            proto = 'ETH'
    except Exception as e:
        info = f'parse_error: {e}'

    return {
        'timestamp': getattr(pkt, 'time', None),
        'src_ip': src_ip,
        'dst_ip': dst_ip,
        'protocol': proto,
        'src_port': src_port,
        'dst_port': dst_port,
        'length': len(pkt) if hasattr(pkt, '__len__') else None,
        'info': info
    }
