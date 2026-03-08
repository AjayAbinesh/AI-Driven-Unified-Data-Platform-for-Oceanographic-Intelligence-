import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

export default function WaveChart({ data }) {

  return (
    <LineChart width={600} height={300} data={data}>
      <XAxis dataKey="timestamp"/>
      <YAxis/>
      <Tooltip/>
      <CartesianGrid stroke="#ccc"/>
      <Line type="monotone" dataKey="wave_height" stroke="#0077ff"/>
      <Line type="monotone" dataKey="prediction" stroke="#ff7300"/>
    </LineChart>
  );
}