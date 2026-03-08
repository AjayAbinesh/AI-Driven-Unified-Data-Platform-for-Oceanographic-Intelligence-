export default function StatsCard({ title, value }) {
  return (
    <div style={{
      background:"#fff",
      padding:"20px",
      borderRadius:"10px",
      boxShadow:"0 2px 6px rgba(0,0,0,0.1)",
      textAlign:"center"
    }}>
      <h3>{title}</h3>
      <h1>{value}</h1>
    </div>
  );
}