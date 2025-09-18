import React from 'react';

export default function PacketTable({packets=[], loading=false}){
  return (
    <div className="card">
      <h3>Packets ({packets.length})</h3>
      {loading ? <div>Loading...</div> : null}
      <table className="table">
        <thead>
          <tr><th>Time</th><th>Src</th><th>Dst</th><th>Proto</th><th>Sport</th><th>Dport</th><th>Len</th></tr>
        </thead>
        <tbody>
          {packets.map((p, idx) => (
            <tr key={idx}>
              <td>{p.timestamp ? new Date(p.timestamp * 1000).toLocaleString() : '-'}</td>
              <td>{p.src_ip || '-'}</td>
              <td>{p.dst_ip || '-'}</td>
              <td>{p.protocol || '-'}</td>
              <td>{p.src_port || '-'}</td>
              <td>{p.dst_port || '-'}</td>
              <td>{p.length || '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
