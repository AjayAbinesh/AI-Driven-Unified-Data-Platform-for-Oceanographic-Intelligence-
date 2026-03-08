export default function RiskIndicator({ risk }) {

  const color =
    risk === "High" ? "red" :
    risk === "Medium" ? "orange" :
    "green";

  return (
    <div style={{
      padding:"20px",
      borderRadius:"10px",
      background:color,
      color:"white",
      textAlign:"center"
    }}>
      <h2>Risk Level</h2>
      <h1>{risk}</h1>
    </div>
  );
}