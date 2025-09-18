from backend.app.parser import parse_packet_dict
def test_parse_mock_packet():
    pkt = {'timestamp': 123.4, 'src_ip': '1.1.1.1', 'dst_ip': '2.2.2.2', 'protocol': 'TCP', 'src_port': 1234, 'dst_port': 80, 'length': 128}
    parsed = parse_packet_dict(pkt)
    assert parsed['src_ip'] == '1.1.1.1'
    assert parsed['dst_port'] == 80
