// src/components/AnalyticsChart.js

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from 'recharts';

export default function AnalyticsChart({ data }) {
  if (!data || data.length === 0) {
    return (
      <div className="bg-white p-4 rounded-xl shadow">
        <p className="text-gray-500 text-center">No billing data available.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h3 className="text-lg font-semibold mb-4 text-gray-800">Billing Trend</h3>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis tickFormatter={(val) => `$${val}`} />
          <Tooltip formatter={(val) => `$${val}`} />
          <Line type="monotone" dataKey="cost" stroke="#6366f1" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
