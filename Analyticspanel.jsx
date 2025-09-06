import { Pie } from 'react-chartjs-2';

const data = {
  labels: ['Positive', 'Negative', 'Neutral'],
  datasets: [{
    data: [
      stats.sentiment.POSITIVE,
      stats.sentiment.NEGATIVE,
      stats.sentiment.NEUTRAL
    ],
    backgroundColor: ['#4caf50', '#f44336', '#ff9800']
  }]
};

<Pie data={data} />
