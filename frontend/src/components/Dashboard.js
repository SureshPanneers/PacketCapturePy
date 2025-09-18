import React from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts';

const COLORS = ['#0088FE','#00C49F','#FFBB28','#FF8042','#A28FFF','#FF6B6B'];

export default function Dashboard({stats={}}){
  const data = Object.keys(stats).map((k,i)=>({ name: k, value: stats[k] }));
  return (
    <div className="card">
      <h3>Protocol Breakdown</h3>
      <div style={{ width: '100%', height: 220 }}>
        <ResponsiveContainer>
          <PieChart>
            <Pie data={data} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80} label>
              {data.map((entry, index) => <Cell key={`c-${index}`} fill={COLORS[index % COLORS.length]} />)}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
