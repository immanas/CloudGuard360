import { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import SummaryCard from './components/SummaryCard';
import UsageTable from './components/UsageTable';
import AnalyticsChart from './components/AnalyticsChart';

function App() {
  const [usageData, setUsageData] = useState([]);
  const [billingData, setBillingData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await axios.get(
          'https://3vd6bli65c.execute-api.ap-south-1.amazonaws.com/prod/data' //working API
        );
        setUsageData(res.data.usage || []);
        setBillingData(res.data.billing || []);
      } catch (err) {
        console.error('Error fetching data:', err);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="bg-gray-100 min-h-screen p-6">
      <Header />
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
        <SummaryCard
          title="EC2 Usage"
          value="12 Instances"
          icon="🖥️"
          color="border-blue-500"
        />
        <SummaryCard
          title="S3 Storage"
          value="150 GB"
          icon="📦"
          color="border-green-500"
        />
        <SummaryCard
          title="Total Monthly Cost"
          value="$160.30"
          icon="💰"
          color="border-yellow-500"
        />
      </section>
      <section className="mt-8">
        <UsageTable data={usageData} />
      </section>
      <section className="mt-8">
        <AnalyticsChart data={billingData} />
      </section>
    </div>
  );
}

export default App;
