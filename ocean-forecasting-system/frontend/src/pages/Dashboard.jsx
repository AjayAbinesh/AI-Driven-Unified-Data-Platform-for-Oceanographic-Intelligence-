import { useEffect, useState } from "react";
import { getHistory, getLive } from "../api";

import WaveChart from "../components/WaveChart";
import RiskIndicator from "../components/RiskIndicator";
import StatsCard from "../components/StatsCard";

export default function Dashboard(){

  const [history,setHistory] = useState([]);
  const [live,setLive] = useState({});
  const [risk,setRisk] = useState("Low");

  useEffect(()=>{

    async function loadData(){

      const historyRes = await getHistory();
      setHistory(historyRes.data);

      const liveRes = await getLive();
      setLive(liveRes.data);

      const wave = liveRes.data.wave_height;

      if(wave > 4) setRisk("High");
      else if(wave > 2) setRisk("Medium");
      else setRisk("Low");
    }

    loadData();

    const interval = setInterval(loadData, 60000);

    return ()=> clearInterval(interval);

  },[]);

  return (

    <div style={{padding:"40px"}}>

      <h1>Ocean Monitoring Dashboard</h1>

      <div style={{
        display:"grid",
        gridTemplateColumns:"1fr 1fr 1fr",
        gap:"20px",
        marginBottom:"30px"
      }}>

        <StatsCard
          title="Wave Height"
          value={live.wave_height + " m"}
        />

        <StatsCard
          title="Wind Speed"
          value={live.wind_speed + " m/s"}
        />

        <RiskIndicator risk={risk}/>

      </div>

      <WaveChart data={history}/>

    </div>
  );
}