import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const getHistory = () => API.get("/history");
export const getLive = () => API.get("/live");
export const getForecast = () => API.get("/forecast");