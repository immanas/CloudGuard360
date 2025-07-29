// src/components/SummaryCard.js

export default function SummaryCard({ title, value, icon, color }) {
  return (
    <div className={`flex items-center gap-4 bg-white shadow rounded-xl p-4 border-l-4 ${color}`}>
      <div className="text-3xl">{icon}</div>
      <div>
        <h2 className="text-md font-semibold text-gray-600">{title}</h2>
        <p className="text-xl font-bold">{value}</p>
      </div>
    </div>
  );
}