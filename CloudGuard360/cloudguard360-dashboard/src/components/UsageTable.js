// src/components/UsageTable.js

export default function UsageTable({ data }) {
  if (!data || data.length === 0) {
    return (
      <div className="bg-white p-4 rounded-xl shadow">
        <p className="text-gray-500 text-center">No usage data available.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h3 className="text-lg font-semibold mb-3 text-gray-800">Service Usage Summary</h3>
      <table className="w-full text-sm text-left border-t border-gray-200">
        <thead className="text-gray-600 uppercase">
          <tr>
            <th className="py-2">Service</th>
            <th className="py-2">Usage</th>
            <th className="py-2">Cost</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, i) => (
            <tr key={i} className="border-t hover:bg-gray-50">
              <td className="py-2">{item.service}</td>
              <td className="py-2">{item.usage}</td>
              <td className="py-2">{item.cost}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
