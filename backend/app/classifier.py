# Simple heuristic classifier + ML stub
from typing import Dict

def classify_packet(parsed_pkt: Dict) -> str:
    \"\"\"Return a label for a parsed packet (simple heuristics).\"\"\"
    proto = (parsed_pkt.get('protocol') or '').upper()
    dport = parsed_pkt.get('dst_port')
    sport = parsed_pkt.get('src_port')

    # heuristics
    if proto in ('HTTP',) or dport in (80, 8080):
        return 'HTTP'
    if proto in ('DNS',) or dport == 53:
        return 'DNS'
    if proto == 'UDP' and dport and dport < 1024:
        return 'SERVICE_UDP'
    if proto == 'TCP' and dport in (22, 23):
        return 'SSH_OR_TELNET'
    if proto == 'ICMP':
        return 'ICMP'
    # fallback
    return proto or 'UNKNOWN'

def train_ml_model(X, y):
    \"\"\"A small stub demonstrating how you could train an sklearn model.
    Not used by default. X and y must be prepared feature arrays and labels.\"\"\"
    try:
        from sklearn.ensemble import RandomForestClassifier
    except Exception:
        raise RuntimeError('scikit-learn not installed')

    clf = RandomForestClassifier(n_estimators=20, random_state=42)
    clf.fit(X, y)
    return clf
