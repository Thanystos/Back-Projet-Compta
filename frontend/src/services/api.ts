import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export const getHealth = async () => {
  const res = await api.get("/health");
  return res.data;
};
