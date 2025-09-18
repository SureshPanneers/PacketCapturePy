from backend.app.classifier import classify_packet
def test_classifier_http():
    pkt = {'protocol': 'TCP', 'dst_port': 80}
    label = classify_packet(pkt)
    assert label == 'HTTP' or label == 'TCP'
