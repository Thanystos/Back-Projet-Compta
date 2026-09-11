import { BrowserRouter, Routes, Route } from "react-router-dom";
import Health from "../pages/Health";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Health />} />
      </Routes>
    </BrowserRouter>
  );
}
