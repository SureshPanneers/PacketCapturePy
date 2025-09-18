const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/api';

export async function fetchStats(){
  const res = await fetch(`${API_BASE}/stats`);
  return res.json();
}

export async function fetchCapture(count=5, mode='mock'){
  const res = await fetch(`${API_BASE}/capture?count=${count}&mode=${mode}`);
  return res.json();
}

export async function fetchPackets(limit=100){
  const res = await fetch(`${API_BASE}/packets?limit=${limit}`);
  return res.json();
}

export async function uploadPcap(file){
  const fd = new FormData();
  fd.append('file', file);
  const res = await fetch(`${API_BASE}/upload_pcap`, { method: 'POST', body: fd });
  return res.json();
}
