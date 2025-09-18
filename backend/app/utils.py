# small utility functions for the backend
def summarize_protocols(parsed_packets):
    counts = {}
    for p in parsed_packets:
        proto = p.get('protocol') or 'UNKNOWN'
        counts[proto] = counts.get(proto, 0) + 1
    return counts
