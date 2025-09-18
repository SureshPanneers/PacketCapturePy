import React, { useEffect, useState } from 'react';
import { fetchStats, fetchCapture, fetchPackets, uploadPcap } from './api';
import Dashboard from './components/Dashboard';
import PacketTable from './components/PacketTable';

export default function App(){
  const [stats, setStats] = useState({});
  const [packets, setPackets] = useState([]);
  const [loading, setLoading] = useState(false);

  async function refresh(){
    setLoading(true);
    const s = await fetchStats();
    setStats(s.stats || {});
    const p = await fetchPackets(200);
    setPackets(p.packets || []);
    setLoading(false);
  }

  useEffect(()=>{ refresh(); }, []);

  async function handleCapture(mode='mock'){
    setLoading(true);
    const res = await fetchCapture(10, mode);
    setPackets(res.packets || []);
    const s = await fetchStats();
    setStats(s.stats || {});
    setLoading(false);
  }

  async function handleUpload(e){
    const file = e.target.files[0];
    if(!file) return;
    setLoading(true);
    const res = await uploadPcap(file);
    setPackets(res.packets || []);
    setLoading(false);
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Network Packet Analysis Dashboard</h1>
        <div className="controls">
          <button onClick={()=>handleCapture('mock')}>Capture (mock)</button>
          <button onClick={()=>handleCapture('real')}>Capture (real)</button>
          <input type="file" accept=".pcap" onChange={handleUpload} />
          <button onClick={refresh}>Refresh</button>
        </div>
      </header>
      <main>
        <Dashboard stats={stats} total={Object.values(stats).reduce((a,b)=>a+b,0)} />
        <PacketTable packets={packets} loading={loading} />
      </main>
    </div>
  );
}
